from django.db import models


class CustomQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_active=False)


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, self._db).filter(is_active=True)