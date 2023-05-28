from django.urls import include, path
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView,ProduitAPIView



urlpatterns = [ 
 path('', views.index, name='index'),
 path('fournisseurs/', views.fournisseur, name='fournisseur'),
 path('search/', views.search, name='search'),
 path('register/',views.register, name = 'register'), 
 path('addfournisseur/', views.addfournisseur, name='addfournisseur'),
 path('addproduct/', views.addproduct, name='addproduct'),
 path('api/category/', CategoryAPIView.as_view()),
 path('api/produits/', ProduitAPIView.as_view()),
 

]
