# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-05 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/question.jpg', upload_to='images/'),
        ),
    ]