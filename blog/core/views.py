# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 19/06/2015

#--------------//////////----------------------

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from blog.core.models import Article

# Create your views here.

class ArticlesViews(ListView):
    model = Article
    template_name = 'index.html'

class ArticleViews(DetailView):
    model = Article
    template_name = 'artigo.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleViews, self).get_context_data(**kwargs)
        return context

