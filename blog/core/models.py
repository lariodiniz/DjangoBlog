# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


import datetime

class Article(models.Model):
    title=models.CharField(_('Titulo'), max_length=100)
    content=models.TextField(_('Conteudo'))
    date=models.DateTimeField(_('Data'), default=datetime.datetime.now(), blank=True)
    slug = models.SlugField(_('slug'),max_length=100, blank=True, unique=True)
    description=models.CharField(_(u'Descrição'), max_length=250, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = _(u'Artigo')
        verbose_name_plural = _(u'Artigos')

    def get_absolute_url(self):

        return reverse('detalhe-do-artigo', kwargs={'slug': self.slug})

def article_pre_save(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente. Ele verifica se ja existe um
    artigo com o mesmo slug e acrescenta um numero ao final para evitar
    duplicidade"""
    if not instance.slug:
        slug = slugify(instance.title)
        novo_slug = slug
        contador = 0

        while Article.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)

        instance.slug = novo_slug

signals.pre_save.connect(article_pre_save, sender=Article)