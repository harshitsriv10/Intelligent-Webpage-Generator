# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20171109_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiledetails',
            old_name='college',
            new_name='institute',
        ),
        migrations.RenameField(
            model_name='profiledetails',
            old_name='joining_year',
            new_name='office',
        ),
        migrations.RemoveField(
            model_name='profiledetails',
            name='room_no',
        ),
    ]