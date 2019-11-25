# -*- coding: utf-8 -*-
from django import forms
from comum.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class NovoDepoimentoForm(forms.ModelForm):
    endereco = forms.CharField(label=_("Endereco"))
    class Meta:
        model = Depoimentos
        fields = ('titulo', 'conteudo', 'tipo', 'document')
        labels = {
            'titulo': u"Título",
            'conteudo': u"Conteúdo",
            'tipo': u"Tipo",
            'document':"Anexe uma imagem",
        }

class NovaRotaForm(forms.ModelForm):
    horario = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                                           attrs={'class': 'form-control'}),
                                    input_formats=('%H:%M',), label="Dia/Hora", required=True)
    class Meta:
        model = RotasDeInteresse
        fields = ('localizacao_atual', 'localizacao_final', 'horario')
        labels = {
            'localizacao_atual': u"De",
            'localizacao_final': u"Até",
            'horario': u"Horário",
        }


class NovoPontoForm(forms.ModelForm):
    horario = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                                           attrs={'class': 'form-control'}),
                                    input_formats=('%H:%M',), label="Dia/Hora", required=True)
    class Meta:
        model = PontosDeInteresse
        fields = ('localizacao', 'horario')
        labels = {
            'localizacao': u"Local",
            'horario': u"Horário",
        }


class CaronaForm(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y',
                                                           attrs={'class': 'form-control'}),
                                    input_formats=('%d/%m/%Y',), label="Data", required=True)
    ponto_embarque = forms.ChoiceField(choices=[(None, "------")], label="Ponto de Embarque",
                                              widget=forms.Select(attrs={"class": "form-control"}))
    class Meta:
        model = Carona
        fields = ('data', 'destino', 'ponto_embarque')
        labels = {
            'destino': u"Destino",
            "data": "Data"
        }

    def __init__(self, usuario, *args, **kwargs):
        super(CaronaForm, self).__init__(*args, **kwargs)
        rotas_qs = RotasDeInteresse.objects.filter(usuario=usuario)
        pontos_qs = PontosDeInteresse.objects.filter(usuario=usuario)
        rotas = [u"Às %s em %s até %s"
            %(str(r.horario), r.localizacao_atual.split(',')[0], r.localizacao_final.split(',')[0]) for r in rotas_qs]
        pontos = [u"Às %s em %s"%(str(p.horario), p.localizacao.split(',')[0]) for p in pontos_qs]
        dictionary = dict(zip(pontos + rotas, pontos + rotas))
        lista = [(k, v) for k, v in dictionary.items()] 

        self.fields['ponto_embarque'].choices = lista


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
