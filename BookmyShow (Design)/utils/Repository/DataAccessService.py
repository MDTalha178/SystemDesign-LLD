from typing import Type, TypeVar
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet, Model

from utils.Repository.Interface import DataObjectLayerInterface

# Define a generic type variable bound to Django Model.
T = TypeVar('T', bound=Model)


class DataAccessService(DataObjectLayerInterface[T]):
    """
    DataAccessService - Generic reusable data access layer (DAL) for Django models.

    Purpose:
        - Provides a standard implementation of the DataObjectLayerInterface.
        - Encapsulates CRUD operations (Create, Read, Update, Delete) and idempotent update.
        - Promotes reusability, consistency, and testability across the project.
        - Helps to decouple business logic from direct ORM calls.

    Usage:
        - Instantiate with a Django model:
            user_dao = DataAccessService(User)
        - Then use:
            user_dao.create(...)
            user_dao.get(...)
            user_dao.filter(...)
            user_dao.update(...)
            user_dao.delete(...)
            user_dao.idempotent_update(...)

    Notes for Developers:
        - For advanced queries or custom behavior, you can subclass DataAccessService and extend methods as needed.
        - This pattern supports the Repository and Service Layer principles of Clean Architecture.
        - Can be injected into services for loose coupling and easier unit testing.
    """

    def __init__(self, model: Type[T]):
        """
        Initialize the DataAccessService with a Django model.

        Args:
            model (Type[T]): A Django model class.
        """
        self.model = model

    def create(self, **kwargs) -> T:
        """
        Create a new instance of the model.

        Args:
            **kwargs: Field values for creating the object.

        Returns:
            T: The created model instance.
        """
        instance = self.model.objects.create(**kwargs)
        return instance

    def get(self, **kwargs) -> T:
        """
        Retrieve a single object matching the given filters.

        Args:
            **kwargs: Filter criteria (field=value).

        Returns:
            T: The matching object, or None if not found.
        """
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def filter(self, **kwargs) -> QuerySet[T]:
        """
        Retrieve a QuerySet of objects matching the given filters.

        Args:
            **kwargs: Filter criteria (field=value).

        Returns:
            QuerySet[T]: QuerySet of matching objects.
        """
        return self.model.objects.filter(**kwargs)

    def update(self, instance: T, **kwargs) -> bool:
        """
        Update fields of an existing object.

        Args:
            instance (T): The model instance to update.
            **kwargs: Fields and new values to update.

        Returns:
            bool: True if update was successful.
        """
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return True

    def delete(self, instance: T) -> bool:
        """
        Delete an existing object.

        Args:
            instance (T): The model instance to delete.

        Returns:
            bool: True if delete was successful.
        """
        instance.delete()
        return True

    def idempotent_update(self, idempotent: dict, **kwargs) -> T:
        """
        Perform an idempotent update:
            - If an object matching the idempotent criteria exists, update it.
            - If not, create a new object with those criteria.

        Args:
            idempotent (dict): Fields used to uniquely identify the object (ex: external_id).
            **kwargs: Fields and values to update or set on creation.

        Returns:
            T: The updated or created model instance.
        """
        instance, _ = self.model.objects.update_or_create(
            **idempotent,
            defaults={
                **kwargs
            }
        )
        return instance

    @staticmethod
    def add_many_to_many_field_data(instance: T, attribute, attrs_key: str, data: [T]):
        if hasattr(instance, attrs_key):
            attribute.set(data)

    def get_data_select_related(self, selected_key: tuple, prefetch: tuple, **kwargs):
        return self.model.objects.select_related(*selected_key).get(**kwargs)

    def get_data_with_relations(self, select_related: tuple = (), prefetch_related: tuple = (), **kwargs):
        """
        Most optimized version - applies filters first, then relations.

        Args:
            select_related (tuple/list/str, optional): Fields for select_related
            prefetch_related (tuple/list/str, optional): Fields for prefetch_related
            **kwargs: Filter conditions

        Returns:
            Model instance with applied optimizations
        """
        # Start with filtered queryset
        queryset = self.model.objects.filter(**kwargs)

        # Apply select_related if provided
        if select_related:
            if isinstance(select_related, tuple):
                queryset = queryset.select_related(*select_related)

        # Apply prefetch_related if provided
        if prefetch_related:
            if isinstance(prefetch_related, tuple):
                queryset = queryset.prefetch_related(*prefetch_related)

        # Get the single record (executes optimized query)
        if queryset:
            return queryset.get()
