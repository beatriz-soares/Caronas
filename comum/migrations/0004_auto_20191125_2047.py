# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-25 20:47
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0003_auto_20191125_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carona',
            name='preco',
        ),
        migrations.AddField(
            model_name='carona',
            name='data',
            field=models.DateField(default=datetime.datetime(2019, 11, 25, 20, 47, 59, 645916)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carona',
            name='destino',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='carona',
            name='ponto_embarque',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='pontosdeinteresse',
            name='horario',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='rotasdeinteresse',
            name='horario',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)]),
        ),
    ]
