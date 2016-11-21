# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160721_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendee',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='event',
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['order'], 'verbose_name': 'Event Details', 'verbose_name_plural': 'Event Details'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='meetup_id',
        ),
        migrations.AddField(
            model_name='event',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Attendee',
        ),
    ]
