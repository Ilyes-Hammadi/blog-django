# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='users/profile_image.png', upload_to='users/'),
        ),
    ]