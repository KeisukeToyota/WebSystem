# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20161208_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=255),
        ),
    ]
