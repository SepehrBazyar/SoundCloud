from uuid import uuid4
from django.db import models
from .manager import CustomManager


# Create your models here.
class AbstractBaseModel(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class BaseModel(
    AbstractBaseModel,
    TimeStampMixin,
):
    objects = CustomManager()

    is_deleted = models.BooleanField(default=False, db_index=True)

    def delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
