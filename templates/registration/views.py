from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.forms import ModelForm
from .forms import ProduitForm,CommandeForm,fournisseurForm,UserRegistrationForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Produit, Categorie, Fournisseur, ProduitNC, Commande
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    template = loader.get_template('magasin/mesProduits.html')
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html ', context)


def categorie_list(request):
    template = loader.get_template('magasin/categorie_list.html')
    categories = Categorie.objects.all()
    return render(request, 'magasin/categorie_list.html', {'categories': categories})


def fournisseur_detail(request, fournisseur_id):
    template = loader.get_template('magasin/fournisseur_detail.html')
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    produits = fournisseur.produit_set.all()
    context = {
        'fournisseur': fournisseur,
        'produits': produits,
    }
    return render(request,'magasin/fournisseur_detail.html', context)


def fournisseur_list(request):
    template = loader.get_template('magasin/fournisseur_list.html')
    fournisseurs = Fournisseur.objects.all()
    context = {
        'fournisseurs': fournisseurs
    }
    return render(request, 'magasin/fournisseur_list.html', context)

def produit_detail(request, produit_id):
    template = loader.get_template('magasin/produit_detail.html')
    produit = Produit.objects.get(id=produit_id)
    return render(request, 'magasin/produit_detail.html', {'produit': produit})


def commande_detail(request, commande_id):
    template = loader.get_template('magasin/commande_detail.html')
    commande = Commande.objects.get(id=commande_id)
    produits = commande.produits.all()
    context = {
        'commande': commande,
        'produits': produits,
    }    
    return render(request, 'magasin/commande_detail.html', context)

def commande_list(request):
    template = loader.get_template('magasin/commande_list.html')
    commandes = Commande.objects.all()
    context = {
        'commandes': commandes
    }
    return render(request, 'magasin/commande_list.html', context)

def search(request):
    template = loader.get_template('magasin/search.html')
    query = request.GET.get('q')
    if query:
        produits = Produit.objects.filter(
            Q(libelle__icontains=query) | Q(description__icontains=query)
        )
        categories = Categorie.objects.filter(name__icontains=query)
        context = {
            'produits': produits,
            'categories': categories,
            'query': query  # pass the query to the context
        }
    else:
        context = {
            'produits': None,
            'categories': None,
            'query': None
        }
    return render(request, 'magasin/search.html', context)

def categorie_detail(request, categorie_id):
    template = loader.get_template('magasin/categorie_detail.html')
    # Retrieve the category object with the specified ID or return a 404 error
    categorie = Categorie.objects.get(id=categorie_id)
    # Retrieve all the products that belong to the specified category
    produits = categorie.produit_set.all()
    context = {
        'categorie': categorie,
        'produits': produits,
    }
    return render(request, 'magasin/categorie_detail.html', context)

def addproduct(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
    return render(request,'magasin/majProduits.html',{'form':form})
def addcommande(request):
    if request.method == "POST" :
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/commande/')
    else :
        form = CommandeForm() #créer formulaire vide
    return render(request,'magasin/majCommande.html',{'form':form})
def addfournisseur(request):
    if request.method == "POST" :
        form = fournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/fournisseurs/')
    else :
        form = fournisseurForm() #créer formulaire vide
    return render(request,'magasin/majfournisseurs.html',{'form':form})

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    return render(request, 'registration/register.html', {'form': form})

