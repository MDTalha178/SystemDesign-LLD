import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model that provides common fields for all models.

    Fields:
        created_at (DateTimeField): Timestamp when the object was created.
        updated_at (DateTimeField): Timestamp when the object was last updated.
        is_deleted (BooleanField): Flag for soft deletion.
                                   Instead of deleting records physically, mark them as deleted.
    Usage:
        Inherit this model in any Django model to get these fields automatically.
    """
    # UUID as primary key for improved security and data migration flexibility.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True  # No table will be created for this model.
