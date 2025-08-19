# cuentas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil, name='perfil'),
    path('detalles/', views.detalles_cuenta, name='detalles_cuenta'),
    path('pedidos/', views.pedidos_activos, name='pedidos_activos'),
    path('crud/', views.crud, name='crud'),
]
