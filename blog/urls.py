from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_blog, name='lista_blog'),  
]


