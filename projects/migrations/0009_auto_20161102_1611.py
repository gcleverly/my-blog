# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-02 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20161102_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='images/question.jpg', upload_to='images/'),
        ),
    ]
