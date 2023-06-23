from django.urls import path
from . import views

app_name = 'Django_app'

urlpatterns = [
    path('', views.MainPage, name='MainPage'), 
    path('Cat_Product/', views.CatProduct, name='CatProduct'), 
    path('Dog_Product/', views.DogProduct, name='DogProduct'), 
    path('SALE/', views.Sale, name='SaleProduct'),
   # path('<str:product_id>/', views.Sale, name = 'P_ID')
    
]
