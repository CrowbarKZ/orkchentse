# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storymaker', '0003_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]
