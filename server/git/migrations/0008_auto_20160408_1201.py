# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-08 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('git', '0007_auto_20160408_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='position',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='position',
        ),
        migrations.RemoveField(
            model_name='pullrequest',
            name='position',
        ),
    ]
