# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-05 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
