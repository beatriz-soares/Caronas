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
    horario = forms.DateTimeField(widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M',
                                                           attrs={'class': 'form-control'}),
                                    input_formats=('%d/%m/%Y %H:%M',), label="Dia/Hora", required=True)
    class Meta:
        model = RotasDeInteresse
        fields = ('localizacao_atual', 'localizacao_final', 'horario')
        labels = {
            'localizacao_atual': u"De",
            'localizacao_final': u"Até",
            'horario': u"Dia/Hora",
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

class TipoUsuarioForm(forms.Form):
    tipo = forms.ChoiceField(choices=[(1,'Passageiro'), (2, 'Motorista')], required=True, widget=forms.RadioSelect)

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
    # error_messages = {
    #     'password_mismatch': _("As duas senhas não são iguais"),
    # }

    email = forms.CharField(label=_("Email do Usuário"), required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=_("Senha"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("Confirmação de senha"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=_("Enter the same password as above, for verification."))
    cidade = forms.CharField(label=_("Cidade"), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(label=_("Telefone"), required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.MultipleChoiceField(choices=[(1,'Quero Solicitar uma Carona'), (2, 'Quero Oferecer uma Carona')], required=True, widget=forms.CheckboxSelectMultiple)
    cnh = forms.IntegerField(label=_("CNH"), min_value=0, required=False)
    placa_veiculo = forms.CharField(label=_("Placa do Veículo"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cor_veiculo = forms.CharField(label=_("Cor do Veículo"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ano_veiculo = forms.IntegerField(label=_("Ano do Veículo"), min_value=0, required=False)
    modelo_veiculo = forms.CharField(label=_("Veículo"), required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

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
                "As duas senhas precisam ser iguais"
            )
        return password2

    def clean(self):
        tipo = self.cleaned_data.get("tipo", None)
        cnh = self.cleaned_data.get("cnh", None)
        placa_veiculo = self.cleaned_data.get("placa_veiculo", None)
        cor_veiculo = self.cleaned_data.get("cor_veiculo", None)
        ano_veiculo = self.cleaned_data.get("ano_veiculo", None)
        modelo_veiculo = self.cleaned_data.get("modelo_veiculo", None)
        if not tipo:
            raise forms.ValidationError(
                "Você precisa selecionar se deseja ser Passageiro ou Motorista"
            )

        if '2' in tipo:
            if not (cnh and placa_veiculo and cor_veiculo and ano_veiculo and modelo_veiculo):
                raise forms.ValidationError(
                    u"Preencha todas as informações sobre o Motorista"
                )

        return self.cleaned_data

    def save(self, commit=True):
        cnh = self.cleaned_data.get("cnh", None)
        placa_veiculo = self.cleaned_data.get("placa_veiculo", None)
        cor_veiculo = self.cleaned_data.get("cor_veiculo", None)
        ano_veiculo = self.cleaned_data.get("ano_veiculo", None)
        modelo_veiculo = self.cleaned_data.get("modelo_veiculo", None)
        cidade = self.cleaned_data.get("cidade", None)
        telefone = self.cleaned_data.get("telefone", None)
        tipo = self.cleaned_data.get("tipo", None)

        # user = super(NovoUserForm, self).save(commit=False)
        usuario = Usuario()
        motorista = Motorista()
        passageiro = Passageiro()
        usuario.set_password(self.cleaned_data["password1"])
        usuario.username = self.cleaned_data.get("username", None)
        usuario.email=self.cleaned_data["email"]
        usuario.is_active = True
        usuario.is_superuser = False

        # user.save()

        usuario.telefone = telefone
        usuario.cidade = cidade
        usuario.save()

        if len(tipo) == 1:
            if '2' in tipo:
                veiculo = Veiculo.objects.create(placa=placa_veiculo, cor=cor_veiculo, modelo=modelo_veiculo, ano=ano_veiculo)
                motorista.usuario = usuario
                motorista.veiculo = veiculo
                motorista.save()
            elif '1' in tipo:
                passageiro.usuario = usuario
                passageiro.save()
        else:
            veiculo = Veiculo.objects.create(placa=placa_veiculo, cor=cor_veiculo, modelo=modelo_veiculo, ano=ano_veiculo)
            motorista.usuario = usuario
            motorista.veiculo = veiculo
            motorista.save()
            passageiro.usuario = usuario
            passageiro.save()

        return usuario
