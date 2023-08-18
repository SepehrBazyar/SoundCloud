from django.db import models
from core.models import BaseModel


# Create your models here.
class Album(BaseModel):
    name = models.CharField(max_length=128)
    rating = models.PositiveSmallIntegerField()
    release_date = models.DateField()
    artist = models.ForeignKey(
        "persons.Person",
        on_delete=models.CASCADE,
        related_name="albums",
    )

    def show(self):
        return f"{self.name} ({self.release_date.year})"

    def __str__(self):
        return f"{self.name} ({self.release_date.year})"


class Track(BaseModel):
    title = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="tracks",
    )

    def __str__(self):
        return f"{self.order}. {self.title} ({self.duration}s)"

    class Meta:
        ordering = ["order"]
        unique_together = [
            ["album", "order"],
        ]
