# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161010_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/question.jpg', upload_to='assets/images'),
        ),
    ]