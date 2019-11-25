# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-25 17:55
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('comum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Carona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponto_embarque', models.CharField(max_length=30)),
                ('destino', models.TextField()),
                ('preco', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnh', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Passageiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carona', models.ManyToManyField(to='comum.Carona')),
            ],
        ),
        migrations.CreateModel(
            name='PontosDeInteresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=50)),
                ('horario', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RotasDeInteresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao_atual', models.CharField(max_length=50)),
                ('localizacao_final', models.CharField(max_length=50)),
                ('horario', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefone', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=35)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('cor', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('ano', models.IntegerField(validators=[django.core.validators.MinValueValidator(2008), django.core.validators.MaxValueValidator(2020)])),
            ],
        ),
        migrations.AddField(
            model_name='rotasdeinteresse',
            name='usuario',
            field=models.ManyToManyField(to='comum.Usuario'),
        ),
        migrations.AddField(
            model_name='pontosdeinteresse',
            name='usuario',
            field=models.ManyToManyField(to='comum.Usuario'),
        ),
        migrations.AddField(
            model_name='passageiro',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comum.Usuario'),
        ),
        migrations.AddField(
            model_name='motorista',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comum.Usuario'),
        ),
        migrations.AddField(
            model_name='motorista',
            name='veiculo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='comum.Veiculo'),
        ),
        migrations.AddField(
            model_name='carona',
            name='motorista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comum.Motorista'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='motorista',
            field=models.ManyToManyField(to='comum.Motorista'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='passageiro',
            field=models.ManyToManyField(to='comum.Passageiro'),
        ),
    ]