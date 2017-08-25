# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eape', '0003_pagamento_valor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='cod_turma',
            new_name='turma',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='cod_Aluno',
            new_name='aluno',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='cod_Turma',
            new_name='turma',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='cod_curso',
            new_name='curso',
        ),
        migrations.AlterField(
            model_name='turma',
            name='diasDaSemana',
            field=models.CharField(choices=[('SegundaQuarta', 'Segunda e Quarta'), ('TercaQuinta', 'Terça e Quinta'), ('TercaQuintaSexta', 'Terça, Quinta e Sexta'), ('Sexta', 'Sexta'), ('Sabado', 'Sabado')], max_length=200),
        ),
        migrations.AlterField(
            model_name='turma',
            name='horario',
            field=models.TimeField(blank=True, verbose_name='horario'),
        ),
    ]
