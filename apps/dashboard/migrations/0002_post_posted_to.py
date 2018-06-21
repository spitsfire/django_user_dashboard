# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts_for', to='dashboard.User'),
            preserve_default=False,
        ),
    ]
