# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ubicacion', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batchs',
            },
        ),
        migrations.CreateModel(
            name='Cinta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cinta',
                'verbose_name_plural': 'Cintas',
            },
        ),
    ]
