# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 19/06/2015

#--------------//////////----------------------

from django.contrib.syndication.views import Feed


from core.models import Article

class LastFiles(Feed):
    title = 'Ultimos artigos'
    link = '/ultimos/'


    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description


    # def item_link(self, item):
    #   return  '/artigo/%d/'%item.id


