# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):
    title=models.CharField(_('Titulo'), max_length=100)
    content=models.TextField(_('Conteudo'))
    date=models.DateTimeField(_('Data'))

    def __unicode__(self):
        return self.title
