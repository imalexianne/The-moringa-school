# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=5, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
