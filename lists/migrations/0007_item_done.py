# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20170718_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
