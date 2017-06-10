from django.db import models

from .base import BaseModel


class Story(BaseModel):
    """
    Represnts a story
    """
    title = models.CharField(max_length=255)
    cover = models.ImageField(
        max_length=1024,
        upload_to='story_covers',
        null=True,
        blank=True
    )
    world_map = models.ImageField(
        max_length=1024,
        upload_to='world_maps',
        null=True,
        blank=True
    )
    start = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.title


class Event(BaseModel):
    """
    Represents a single event in a story

    - Events tie together and form a graph of a story
    - Each event has a title, a picture, text, and choices
    - Each event leads to another event based on choice and some stats
    """
    title = models.CharField(max_length=255)
    picture = models.ImageField(max_length=1024, upload_to='story_pics',
                                null=True, blank=True)

    # location on the map
    x = models.IntegerField()
    y = models.IntegerField()

    text = models.TextField()

    def __str__(self):
        return self.title


class Choice(BaseModel):
    """
    Represents 1 choice a player can make in an event
    """
    event_from = models.ForeignKey('Event', on_delete=models.CASCADE,
                                   related_name='choices')
    title = models.CharField(max_length=255)

    visible_if = models.TextField()
    sucess_if = models.TextField()
    success_event_to = models.ForeignKey('Event', on_delete=models.CASCADE,
                                         related_name='+')
    fail_event_to = models.ForeignKey('Event', on_delete=models.CASCADE,
                                      related_name='+')

    def __str__(self):
        return self.title
