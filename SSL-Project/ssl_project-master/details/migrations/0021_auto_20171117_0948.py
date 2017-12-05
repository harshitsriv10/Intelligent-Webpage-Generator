# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-17 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0020_studentsdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='co_pi',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='pi',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentsdetails',
            name='student_status',
            field=models.CharField(choices=[('Continuing', 'Continuing'), ('Completed', 'Completed')], max_length=255),
        ),
    ]