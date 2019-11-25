# -*- coding: utf-8 -*-
from django import forms
from comum.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class NovoDepoimentoForm(forms.ModelForm):
    # document = forms.FileField(required=False)
    class Meta:
        model = Depoimentos
        fields = ('titulo', 'conteudo', 'tipo', 'document')
        labels = {
            'titulo': u"Título",
            'conteudo': u"Conteúdo",
            'tipo': u"Tipo",
            'document':"Anexe uma imagem",
        }

class FiltroDepoimentoForm(forms.Form):
    tipo = forms.ModelChoiceField(TipoDepoimentos.objects.all(), required=False)

class NovoTipoDepoimentoForm(forms.ModelForm):
    class Meta:
        model = TipoDepoimentos
        fields = ('nome',)
        labels = {
            'nome': u"Nome",
        }

class NovoUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': u"Usuário",
            'password': "Senha"
        }

class NovoUserForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("As duas senhas não são iguais"),
    }
    password1 = forms.CharField(label=_("Senha"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Confirmação de senha"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_("Enter the same password as above, for verification."))
    class Meta:
        model = User
        fields = ("username",)
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(NovoUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.is_superuser = False
        if commit:
            user.save()
        return user
