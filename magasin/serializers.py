from rest_framework.serializers import ModelSerializer
from magasin.models import Categorie,Produit
from rest_framework import viewsets


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']

class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libellé','description','catégorie']
        
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
