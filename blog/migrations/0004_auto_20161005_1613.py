# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-05 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161005_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/question.jpg', upload_to=''),
        ),
    ]
