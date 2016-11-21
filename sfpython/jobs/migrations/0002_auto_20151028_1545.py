# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='lengthy_details',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.SlugField(default='/'),
            preserve_default=False,
        ),
    ]
