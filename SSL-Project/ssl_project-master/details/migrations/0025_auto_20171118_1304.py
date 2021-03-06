# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-18 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0024_auto_20171117_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(max_length=255)),
                ('files', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='project_description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recognitiondetails',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='teachingdetails',
            name='course_description',
            field=models.TextField(max_length=255),
        ),
        migrations.AddField(
            model_name='coursedetails',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.TeachingDetails'),
        ),
    ]
