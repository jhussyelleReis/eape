import uuid
from django.db import models
from django.utils import timezone


# Modelos Espaco Artistico

DIAS = (('SegundaQuarta',u'Segunda e Quarta'), ('TercaQuinta',u'Terça e Quinta'), ('TercaQuintaSexta',u'Terça, Quinta e Sexta'),('Sexta',u'Sexta'),('Sabado','Sabado'))

DIAPAGAMENTO = (('5','05'),('15','15'),('25','25'))

TURNO = (('Manha',u'Manha'),('Tarde','Tarde'),('Noite','Noite'))


class Aluno(models.Model):
    matricula = models.CharField(max_length=200)
    data_matricula = models.DateTimeField(blank=True, null=True) 
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    contato = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=200)
    turma = models.ForeignKey('Turma')
    tipo_pagamento = models.CharField(max_length=200)
    diaDoPagamento = models.CharField(max_length=100, choices=DIAPAGAMENTO)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    diasDaSemana = models.CharField(max_length=200, choices=DIAS)
    turno = models.CharField(max_length=100, choices=TURNO)
    horario = models.TimeField((u'horario'), blank=True)   
    curso = models.ForeignKey('Curso')

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    aluno = models.ForeignKey('Aluno')
    turma = models.ForeignKey('Turma')
    data_realizacao = models.DateTimeField(blank=True, null=True) 
    valor = models.DecimalField(max_digits = 5 ,  decimal_places = 2 )

    def __unicode__(self):
        return self.data_realizacao

