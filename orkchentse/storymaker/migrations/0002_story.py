# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storymaker', '0001_story_maker_first_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(blank=True, max_length=1024, null=True, upload_to='story_covers')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='storymaker.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]