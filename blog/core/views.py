# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 19/06/2015

#--------------//////////----------------------

from django.shortcuts import render

from django.views.generic import ListView, DetailView, FormView
from blog.core.models import Article
from blog.core.forms import ContactForm

# Create your views here.

class ArticlesViews(ListView):
    model = Article
    template_name = 'core/index.html'

class ArticleViews(DetailView):
    model = Article
    template_name = 'core/artigo.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleViews, self).get_context_data(**kwargs)
        return context

class ContactViews(FormView):
    template_name = 'core/contato.html'
    form_class = ContactForm
    success_url = 'thanks'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)


