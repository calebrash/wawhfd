# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wawhfd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
