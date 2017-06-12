from django.shortcuts import render, reverse

from ..models.character import Character
from ..models.story import Choice


def story(request, choice_id=-1):
    character = Character.objects.all().first()
    if choice_id == -1:
        event = character.current_event or character.story.start
    else:
        event = handle_choice(int(choice_id))

    # prepare context
    title = event.title
    picture_url = event.picture.source.url if event.picture else None
    text = event.text

    choices = []
    for choice in event.choices.all():
        choice_url = reverse('handle_choice', kwargs={'choice_id': choice.pk})
        choices.append((choice.title, choice_url))

    return render(request, 'storymaker/event.html', {
        'title': title,
        'picture_url': picture_url,
        'text': text,
        'choices': choices,
    })


def handle_choice(choice_id):
    """
    Processes choice and returns event to redirect to
    """
    choice = Choice.objects.get(pk=choice_id)
    return choice.success_event_to

