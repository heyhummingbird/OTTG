# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_item_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False, unique=True),
        ),
    ]
