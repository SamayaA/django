from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id']
    search_fields = ['title', 'description']

class StockSearchFilter(SearchFilter):
    def __init__(self):
        super.__init__
    search_param = 'products'

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.DjangoFilterBackend, StockSearchFilter]
    filterset_fields = ["id", "address"]
    search_fields = ["products__title", "products__description", "products__id"]

