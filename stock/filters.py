import django_filters
from django_filters import CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta :
        model = Order
        fields = '__all__'
        exclude = ['quantity', 'price', 'date_created']

class PurchaseFilter(django_filters.FilterSet):
    class Meta :
        model = Purchase
        fields = '__all__'
        exclude = ['quantity', 'price', 'date_created']

class ProductFilter(django_filters.FilterSet):
    name = CharFilter(label="",field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name']