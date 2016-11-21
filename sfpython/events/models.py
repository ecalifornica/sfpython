from django.db import models

from adminsortable.models import SortableMixin

class Event(SortableMixin):
    class Meta:
        verbose_name = 'Event Details'
        verbose_name_plural = 'Event Details'
        ordering = ['order']
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=255)
    details = models.TextField()
    link = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title
