from django.db import models
from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Faq

class FaqAdmin(SortableAdmin):
    prepopulated_fields = {"url": ("question",)}
    list_display = ('question', 'display')
    list_filter = ('display',)

admin.site.register(Faq, FaqAdmin)
