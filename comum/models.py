# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Usuario(User):
    telefone = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=35)


class PontosDeInteresse(models.Model):
    localizacao = models.CharField(max_length=250)
    horario = models.DateTimeField(auto_now=True, auto_now_add=False)
    usuario = models.ManyToManyField(Usuario)


class RotasDeInteresse(models.Model):
    localizacao_atual = models.CharField(max_length=250)
    localizacao_final = models.CharField(max_length=250)
    horario = models.DateTimeField()
    usuario = models.ManyToManyField(Usuario)
    

class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    ano = models.IntegerField(validators=[MinValueValidator(2008), MaxValueValidator(2020)])
    

class Motorista(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cnh = models.CharField(max_length=11)
    veiculo = models.OneToOneField(Veiculo, on_delete=models.CASCADE)


class Carona(models.Model):
    ponto_embarque = models.CharField(max_length=30)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    destino = models.TextField()
    preco = models.FloatField()


class Passageiro(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    carona = models.ManyToManyField(Carona)


class Avaliacao(models.Model):
    nota = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    motorista = models.ManyToManyField(Motorista)
    passageiro = models.ManyToManyField(Passageiro)
    

class Comentario(models.Model):
    titulo = models.CharField(max_length=15)
    texto = models.TextField()
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)


# Create your models here.
class TipoDepoimentos(models.Model):
    nome = models.CharField(max_length=30)
    def __unicode__(self):
        return '%s' % (self.nome)
    def __str__(self):
        return '%s' % (self.nome)

class Depoimentos(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey(User)
    tipo = models.ForeignKey(TipoDepoimentos, null=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)

class Comentario(models.Model):
    conteudo = models.CharField(max_length=500)
    autor = models.ForeignKey(User)
    pai = models.ForeignKey(Depoimentos, related_name="comentarios")

class Mensagem(models.Model):
    conteudo = models.CharField(max_length=500)
    autor = models.ForeignKey(User, related_name="mensagens")
    destinatario = models.ForeignKey(User, related_name="destinos")
    lida = models.BooleanField(default=False)
