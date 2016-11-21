# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('question', models.TextField(help_text=b'Question')),
                ('display', models.BooleanField(default=False, help_text=b'Show this faq on the site.')),
                ('url', models.SlugField()),
                ('answer', models.TextField(help_text=b'Response.')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
