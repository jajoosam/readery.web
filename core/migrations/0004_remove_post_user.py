# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
