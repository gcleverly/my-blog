# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-19 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
    ]
