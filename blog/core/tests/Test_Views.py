# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------

from django.test import TestCase
from django.utils import timezone

from blog.core.models import Article

class ArticlesViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("")

    def test_get(self):
        "Acesso a / deve retornar status code 200"
        self.assertEqual(200, self.resp.status_code)

class FeedViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("/rss/ultimos/")

    def test_get(self):
        "Acesso a /rss/ultimos/ deve retornar status code 200"
        self.assertEqual(200, self.resp.status_code)

class ArticleViewsTest(TestCase):
    def setUp(self):
        s = Article.objects.create(
            title="Ola Mundo",
            content="OlaMundo",
            date=timezone.now(),
            description='Primeiro artigo'
        )
        self.resp = self.client.get("/artigo/%d/" %s.pk)

    def test_get(self):
        "Acesso a /artigo/1/ deve retornar status code 200"
        self.assertEqual(200, self.resp.status_code)




