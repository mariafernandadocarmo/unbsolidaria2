# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-10 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unbsolidaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cep',
            field=models.CharField(default=123, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabalho',
            name='autor',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabalho',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='endereco',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='descricao',
            field=models.TextField(max_length=140),
        ),
    ]