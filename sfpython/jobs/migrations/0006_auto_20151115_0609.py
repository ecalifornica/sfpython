# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20151112_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='level',
            field=models.IntegerField(default=0, choices=[(3500, b'Platinum'), (2000, b'Diamond'), (1500, b'Gold'), (1000, b'Silver'), (500, b'Bronze')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='contact_email',
            field=models.EmailField(default=b'', help_text=b'Not shared publicly. Be sure to use the email associated with your Paypal account.', max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='details',
            field=models.TextField(help_text=b'Short and punchy text - 140 chars or less.', verbose_name=b'Summary'),
        ),
        migrations.AlterField(
            model_name='job',
            name='lengthy_details',
            field=models.TextField(help_text=b'The rest of the details.', verbose_name=b'Details', blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='link',
            field=models.CharField(default=b'', help_text=b'Add a link to apply for this job.', max_length=255),
        ),
    ]
