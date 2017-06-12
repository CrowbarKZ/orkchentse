from django.db import models

from .base import BaseModel


class Picture(BaseModel):
    """
    Reusable picture
    """
    name = models.CharField(max_length=255)
    source = models.ImageField(
        max_length=1024,
        upload_to='story_picrures',
    )

    def __str__(self):
        return self.name
