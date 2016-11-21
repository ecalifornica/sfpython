from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Job

class JobAdmin(SortableAdmin):
    prepopulated_fields = {"url": ("title",)}
    list_display = ('title', 'details', 'display', 'level', 'location')
    list_filter = ('display',)

admin.site.register(Job, JobAdmin)
