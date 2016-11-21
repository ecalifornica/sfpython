# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20151115_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default=b'', help_text=b'Employer name.', max_length=255),
        ),
    ]
