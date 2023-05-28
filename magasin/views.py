from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Produit, Fournisseur, Categorie
from .forms import ProduitForm, fournisseurForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from magasin.models import Categorie
from magasin.serializers import CategorySerializer, ProduitSerializer
from django.shortcuts import redirect

@login_required
def index(request):
    template = loader.get_template('magasin/mesProduits.html')
    categories = Categorie.objects.all()
    selected_category = request.GET.get('category')
    query = request.GET.get('q', '')
    if query:
        products = Produit.objects.filter(nom__icontains=query)
        selected_category = None
    elif selected_category:
        products = Produit.objects.filter(catégorie__name=selected_category)
    else:
        products = Produit.objects.all()
    context = {'products': products, 'categories': categories,
               'selected_category': selected_category, 'search_query': query}
    return render(request, 'magasin/mesProduits.html', context)


def search(request):
    query = request.GET.get('q', '')
    products = Produit.objects.filter(libellé__icontains=query)
    context = {'products': products, 'search_query': query}
    return render(request, 'magasin/mesProduits.html', context)


def fournisseur(request):
    template = loader.get_template('magasin/mesFournisseurs.html')
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/mesFournisseurs.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def addproduct(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide
    return render(request, 'magasin/majProduits.html', {'form': form})


def addfournisseur(request):
    if request.method == "POST":
        form = fournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/fournisseurs/')
    else:
        form = fournisseurForm()  # créer formulaire vide
    return render(request, 'magasin/majfournisseurs.html', {'form': form})


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('catégory_id')
        if category_id:
            queryset = queryset.filter(catégorie_id=category_id)
        return queryset
