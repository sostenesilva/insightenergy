from django.urls import path
from . import views

urlpatterns = [
    path('', views.orcamentos, name='orcamentos'),

    path('bancodeirradiacao/', views.bancodeirradiacao, name='banco_de_irradiacao'),
    path('bancodeirradiacao/adicionar/', views.irrad_add, name='irrad_add'),
    path('bancodeirradiacao/editar/<int:irrad_pk>', views.irrad_edit, name='irrad_edit'),
    path('bancodeirradiacao/deletar/<int:irrad_pk>', views.irrad_delet, name='irrad_delet'),


    path('bancodeequipamentos/', views.bancodeequipamentos, name='banco_de_equipamentos'),
    path('bancodeequipamentos/addinversor', views.inversor_add, name='inversor_add'),
    path('bancodeequipamentos/editarinversor/<int:inversor_pk>', views.inversor_edit, name='inversor_edit'),
    path('bancodeequipamentos/deletarinversor/<int:inversor_pk>', views.inversor_delet, name='inversor_delet'),

    path('bancodeequipamentos/addmodulo', views.modulo_add, name='modulo_add'),
    path('bancodeequipamentos/editarmodulo/<int:modulo_pk>', views.modulo_edit, name='modulo_edit'),
    path('bancodeequipamentos/deletarmodulo/<int:modulo_pk>', views.modulo_delet, name='modulo_delet'),


    path('bancodeprecos/', views.bancodeprecos, name='banco_de_precos'),
    path('bancodeprecos/adicionar/', views.bdprecos_add, name='bdprecos_add'),
    path('bancodeprecos/editar/<int:precos_pk>', views.bdprecos_edit, name='bdprecos_edit'),
    path('bancodeprecos/deletar/<int:precos_pk>', views.bdprecos_delet, name='bdprecos_delet'),

    path('historico/', views.historico_orcamentos, name='historico_orcamentos'),
]

