# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='display',
            field=models.BooleanField(default=False, help_text=b'Show this job posting on the site.'),
        ),
        migrations.AlterField(
            model_name='job',
            name='details',
            field=models.TextField(help_text=b'Short and punchy text - 140 chars or less.'),
        ),
        migrations.AlterField(
            model_name='job',
            name='lengthy_details',
            field=models.TextField(help_text=b'The rest of the details.', blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.CharField(help_text=b"Optionally add a link to your company's job site.", max_length=255, blank=True),
        ),
    ]
