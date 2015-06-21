# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from blog.core.views import ArticlesViews, ArticleViews, ContactViews
from blog.feeds import LastFiles


urlpatterns = [
    url(r'^$', ArticlesViews.as_view(), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rss/(?P<url>.*)/$', LastFiles(), name='rss'),
    url(r'^artigo/(?P<slug>[\w_-]+)$', ArticleViews.as_view(), name='detalhe-do-artigo'),
    url(r'^contato/$', ContactViews.as_view(), name='contato'),
    url(r'^static/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
