# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

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
