from django.contrib import admin

from .models.character import Character
from .models.picture import Picture
from .models.story import Story, Event, Choice


# inlines
class ChoiceInline(admin.StackedInline):
    model = Choice
    fk_name = 'event_from'


# normal stuff
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass


