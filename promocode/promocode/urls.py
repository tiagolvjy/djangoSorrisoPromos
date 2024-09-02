from django.contrib import admin
from django.urls import path
from promotions.views import promotions_list, promotion_detail, home  # Adicione a importação da nova view

urlpatterns = [
    path('', home, name='home'),  # Adicione esta linha para a página inicial
    path('promotions/', promotions_list, name='promotions_list'),
    path('promotions/<int:pk>/', promotion_detail, name='promotion_detail'),
]
