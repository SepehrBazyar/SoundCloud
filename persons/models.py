from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import AbstractBaseModel


# Create your models here.
class Person(AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Fan(Person):
    class Meta:
        proxy = True
        verbose_name = _("Fan")
        verbose_name_plural = _("Fans")

    @property
    def followings_count(self) -> int:
        return self.followings.count()


class Artist(Person):
    class Meta:
        proxy = True
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

    @property
    def followers_count(self) -> int:
        return self.followers.count()


class Relation(AbstractBaseModel):
    from_user = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="followings",
    )
    to_user = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="followers",
    )

    class Meta:
        verbose_name = _("Relation")
        verbose_name_plural = _("Relations")
