# coding: utf-8

#--------------//////////----------------------


#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------

from django.test import TestCase
from blog.core.models import Article
from django.utils import timezone

class ArticleTest(TestCase):
    def setUp(self):
        self.obj =Article(
            title="Ola Mundo",
            content="OlaMundo",
            date=timezone.now(),
            description='Primeiro artigo'

        )
    def test_create(self):
        'Testa a criação em uma tabela'
        self.obj.save()
        self.assertEqual(1, self.obj.id)