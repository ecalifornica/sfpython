from django.core.urlresolvers import reverse
from django.db import models

from adminsortable.models import SortableMixin

class VisibleFaqManager(models.Manager):
    def get_queryset(self):
        return super(VisibleFaqManager, self).get_queryset().filter(display=True)

class Faq(SortableMixin):
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['order']
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    question = models.TextField(help_text="Question")
    display = models.BooleanField(help_text="Show this faq on the site.", default=False)
    url = models.SlugField()
    answer = models.TextField(help_text="Response.")

    def get_absolute_url(self):
      return reverse('faq.views.detail', args=[self.url])
      
    def __unicode__(self):
        return self.question

    objects = models.Manager()
    visible = VisibleFaqManager()



