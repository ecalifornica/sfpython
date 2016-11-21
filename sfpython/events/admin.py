from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Event

admin.site.register(Event, SortableAdmin)
