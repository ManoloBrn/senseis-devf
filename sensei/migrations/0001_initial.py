# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-14 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desescuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=255)),
                ('pic', models.ImageField(upload_to='senseis/bio/')),
                ('tel', models.CharField(max_length=15)),
                ('mail', models.CharField(max_length=255)),
                ('cinta', models.ManyToManyField(to='desescuela.Cinta')),
            ],
            options={
                'verbose_name': 'Sensei',
                'verbose_name_plural': 'Senseis',
            },
        ),
    ]
