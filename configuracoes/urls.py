from django.urls import path
from . import views

urlpatterns = [
    path('', views.configuracoes, name='config'),
]