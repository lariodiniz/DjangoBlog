# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------



from django.contrib import admin

from blog.core.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','content')


admin.site.register(Article, ArticleAdmin)
