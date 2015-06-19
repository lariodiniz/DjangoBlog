# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------

from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
class Article(models.Model):
    title=models.CharField(_('Titulo'), max_length=100)
    content=models.TextField(_('Conteudo'))
    date=models.DateTimeField(_('Data'), default=datetime.datetime.now(), blank=True)
    description=models.CharField(_(u'Descrição'), max_length=250, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = _(u'Artigo')
        verbose_name_plural = _(u'Artigos')

    def get_absolute_url(self):
        return   '/artigo/%d/' %self.id
