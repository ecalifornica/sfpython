# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('link', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Event Details',
                'verbose_name_plural': 'Event Details',
            },
        ),
    ]
