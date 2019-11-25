from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^inicio/', views.index, name='index'),
    url(r'^estatistica/', views.estatistica, name='estatistica'),
    url(r'^login/', views.login_aplicacao, name='login'),
    url(r'^logout/', views.logout_aplicacao, name='logout'),
    url(r'^novo_depoimento/', views.novo_depoimento, name='novo_depoimento'),
    url(r'^apagar_depoimento/(?P<id>\d+)/$', views.apagar_depoimento, name='apagar_depoimento'),
    url(r'^novo_comentario/(?P<id>\d+)/$', views.novo_comentario, name='novo_comentario'),
    url(r'^nova_mensagem/(?P<id>\d+)/$', views.nova_mensagem, name='nova_mensagem'),
    url(r'^mensagens/$', views.ver_mensagens, name='mensagens'),
    url(r'^mensagens/(?P<id>\d+)/$', views.mensagens, name='mensagens'),
    url(r'^tipos_depoimento/$', views.tipos_depoimento, name='tipos_depoimento'),
    url(r'^tipos_depoimento/novo/$', views.novo_tipo_depoimento, name='novo_tipo_depoimento'),
    url(r'^novo_usuario/$', views.novo_usuario, name='novo_usuario'),
    url(r'^nova_rota/$', views.nova_rota, name='nova_rota'),
    url(r'^novo_ponto/$', views.novo_ponto, name='novo_ponto'),
    url(r'^novo_pedido_carona/$', views.novo_pedido_carona, name='novo_pedido_carona'),
    url(r'^novo_oferecer_carona/$', views.novo_oferecer_carona, name='novo_oferecer_carona'),
    url(r'^historico/$', views.historico, name='historico'),

]
