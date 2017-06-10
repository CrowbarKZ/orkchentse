from jsonfield import JSONField

from django.conf import settings
from django.db import models

from .base import BaseModel


class Character(BaseModel):
    """
    Represnts player's character
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='characters')
    story = models.ForeignKey('Story', on_delete=models.CASCADE,
                              related_name='characters')
    name = models.CharField(max_length=255)
    current_event = models.ForeignKey(
        'Event',
        on_delete=models.SET_NULL,
        related_name='characters_here',
        null=True,
        blank=True
    )
    last_checkpoint = models.ForeignKey(
        'Event',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )
    stats = JSONField(default={}, blank=True)
    status = JSONField(default={}, blank=True)
    items = JSONField(default={}, blank=True)

    def __str__(self):
        return self.name
