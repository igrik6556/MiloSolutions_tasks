# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='random_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Random number'),
        ),
    ]
