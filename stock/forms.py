from django.forms import ModelForm
from .models import Order, Purchase

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
