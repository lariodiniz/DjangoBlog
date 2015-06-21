# coding: utf-8

#--------------//////////----------------------

#Projeto Criado por: Lário Diniz
#Contatos: developer.lario@gmail.com
#Data: 20/06/2015

#--------------//////////----------------------

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Nome'), max_length=50)
    email = forms.EmailField(label=_('Email'),required=False)
    message = forms.Field(label=_('Mensagem'),widget=forms.Textarea)

    def send_email(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'developer.lario@gmail.com'
        texto = """
        Nome: %(name)s
        E-mail: %(email)s
        Mensagem:
        %(message)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
            )