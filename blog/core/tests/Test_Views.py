# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 15/06/2015

#--------------//////////----------------------

from django.test import TestCase

class ArticleViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get("")

    def test_get(self):
        "Acesso a deve retornar status code 200"
