# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='done',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.Done'),
        ),
    ]
