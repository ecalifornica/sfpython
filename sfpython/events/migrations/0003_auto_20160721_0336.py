# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151028_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rsvp', models.CharField(max_length=10, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Waitlist', b'Waitlist')])),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meetup_id', models.CharField(max_length=255)),
                ('handle', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='order',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='meetup_id',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendee',
            field=models.ForeignKey(to='events.Attendee'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
    ]
