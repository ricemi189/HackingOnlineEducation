# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20170803_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
