from django.db import models
from datetime import datetime
# Create your models here.

class Produit(models.Model):
    type_choices=[("em","emballé"),("fr","Frais"),("cs","Conserve")]
    libellé=models.CharField(max_length=50)
    description=models.TextField(default="Non définie")
    prix=models.DecimalField(max_digits=10, decimal_places=3)
    type=models.CharField(max_length=2,choices=type_choices,default="em")
    img=models.ImageField(blank=True)
    catégorie=models.ForeignKey("Categorie",on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey("Fournisseur",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "\nLibellé : "+self.libellé +"\nDescription : "+self.description+"\nPrix : "+str(self.prix)
class Categorie(models.Model):
    TYPE_CHOICES=[
        ("Alimentaire","Al"), ("Meuble","Mb"),
        ("Sanitaire","Sn"), ("Vaisselle","Vs"),
        ("Vêtement","Vt"),("Jouets","Jx"),
        ("Linge de Maison","Lg"),("Bijoux","Bj"),("Décor","Dc"),
        ("Immobilier","Im"),("Meuble","Me"),("ParaPharmacie","Pp"),
        ("Electroménager","El"),("Frais","Fr"),("Tapis","Ta")]
    name=models.CharField(max_length=50,default="Alimentaire",choices=TYPE_CHOICES)
    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    name=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "\nNom : "+self.name+"\nAdresse : "+self.adresse+"\nEmail : "+self.email+"\nTelephone : "+str(self.telephone)

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=datetime.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produit=models.ManyToManyField('Produit')
    def __str__(self): 
        return "\nDate Commande : "+(self.dateCde).strftime('%Y-%m-%d')+"\nTotal : "+str(self.totalCde)

class ProduitNC(Produit) : 
    Duree_garantie=models.CharField(max_length=100)

class ProduitC(Produit) : 
    Duree_garantie=models.CharField(max_length=100)