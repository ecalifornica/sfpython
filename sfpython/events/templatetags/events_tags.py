from django import template

register = template.Library()

from events.models import Event

@register.assignment_tag()
def get_events():
    return Event.objects.all().order_by("order")
