# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='diaDoPagamento',
            field=models.CharField(choices=[('5', '05'), ('15', '15'), ('25', '25')], default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
