# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20161010_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, to='blog.Image'),
        ),
    ]
