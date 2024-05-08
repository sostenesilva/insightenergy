from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashpage'),
    path('bdacessos/adicionar/', views.acesso_add, name='acesso_add'),
    path('bdacessos/editar/<int:irrad_pk>', views.acesso_edit, name='acesso_edit'),
    path('bdacessos/deletar/<int:irrad_pk>', views.acesso_delet, name='acesso_delet'),
]