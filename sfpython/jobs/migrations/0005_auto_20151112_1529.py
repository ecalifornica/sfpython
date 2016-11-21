# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20151106_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='contact_email',
            field=models.EmailField(default=b'', help_text=b'Not shared publicly.', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_phone',
            field=models.CharField(default=b'', help_text=b'Not shared publicly.', max_length=20),
        ),
    ]
