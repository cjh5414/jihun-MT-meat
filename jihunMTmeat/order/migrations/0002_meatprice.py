# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeatPrice',
            fields=[
                ('name', models.CharField(default='', max_length=254, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
            ],
        ),
    ]