# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eape', '0012_auto_20170825_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_realizacao', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')], max_length=100)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eape.Aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eape.Turma')),
            ],
        ),
    ]
