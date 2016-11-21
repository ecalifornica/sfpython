# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20151115_0609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['order'], 'verbose_name': 'Job Details', 'verbose_name_plural': 'Job Postings'},
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='level',
            field=models.IntegerField(default=0, choices=[(3500, b'Platinum'), (2000, b'Diamond'), (1500, b'Gold'), (1000, b'Silver'), (500, b'Bronze'), (0, b'None')]),
        ),
    ]
