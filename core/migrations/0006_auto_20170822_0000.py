# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='about',
            field=models.CharField(default='', max_length=250),
        ),
    ]