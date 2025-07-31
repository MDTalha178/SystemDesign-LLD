from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from django.db.models import QuerySet, Model

# Define a generic type variable bound to Django Model.
T = TypeVar('T', bound=Model)


class DataObjectLayerInterface(Generic[T], ABC):
    """
    DataObjectLayerInterface - Abstract base class for implementing a consistent data access layer (DAL).

    Purpose:
        - This interface defines the contract for interacting with the database for a specific model type T.
        - Encourages consistent patterns for querying, creating, updating, and deleting records across the project.
        - Helps to decouple business logic from ORM-specific details.
        - Enables testability and flexibility (you can mock/replace implementations easily).

    Key Methods (all abstract → must be implemented by concrete class):
        - filter(**filters): Return a QuerySet of matching objects.
        - get(**filters): Return a single matching object.
        - create(data): Create a new object.
        - update(instance, **kwargs): Update an existing object.
        - delete(id): Delete an object by ID (usually soft delete preferred).
        - idempotent_update(idempotent_key, **kwargs): Update object safely with idempotency support.

    Usage:
        - Inherit this interface when building repositories for a model.
        - Example:
            class UserRepository(DataObjectLayerInterface[User]):
                def filter(self, **filters) -> QuerySet[User]: ...
                def get(self, **filters) -> User: ...
                ...

    Notes for Developers:
        - Follow this pattern when adding new repositories → promotes consistent API across the project.
        - Helps align with Clean Architecture / Domain-Driven Design (DDD) principles.
        - Can be combined with service layers for maximum separation of concerns.

    """

    @abstractmethod
    def filter(self, **filters) -> QuerySet[T]:
        """
        Retrieve a QuerySet of objects matching the given filters.

        Args:
            **filters: Django ORM filter arguments (field=value).

        Returns:
            QuerySet[T]: QuerySet of matching objects.
        """
        raise NotImplementedError("Sub class should implement this method")

    @abstractmethod
    def get(self, **filters) -> T:
        """
        Retrieve a single object matching the given filters.

        Args:
            **filters: Django ORM filter arguments.

        Returns:
            T: A single matching object.

        Raises:
            DoesNotExist, MultipleObjectsReturned
        """
        raise NotImplementedError("Sub class should implement this method")

    @abstractmethod
    def create(self, data: dict) -> T:
        """
        Create a new object.

        Args:
            data (dict): Dictionary of field names and values.

        Returns:
            bool: True if creation was successful, False otherwise.
        """
        raise NotImplementedError("Sub class should implement this method")

    @abstractmethod
    def update(self, instance, **kwargs) -> bool:
        """
        Update an existing object.

        Args:
            instance: The model instance to update.
            **kwargs: Fields and new values to update.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        raise NotImplementedError("Sub class should implement this method")

    @abstractmethod
    def delete(self, id: str) -> bool:
        """
        Delete an object by its ID.

        Args:
            id (str): The unique identifier of the object.

        Returns:
            bool: True if delete was successful, False otherwise.
        """
        raise NotImplementedError("Sub class should implement this method")

    @abstractmethod
    def idempotent_update(self, idempotent, **kwargs):
        """
        Perform an idempotent update.

        Args:
            idempotent: An idempotency key (or similar unique identifier) used to ensure this update can be retried safely.
            **kwargs: Fields and new values to update.

        Returns:
            Depends on implementation (commonly returns bool or updated object).
        """
        raise NotImplementedError("Sub class should implement this method")
