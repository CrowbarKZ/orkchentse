from django.shortcuts import render

from ..models.story import Event


def story(request):
    event = Event.objects.all().first()
    return render(request, 'storymaker/event.html', {
        'event': event,
    })
