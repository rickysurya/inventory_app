from django import forms
from django.forms import ModelForm
from .models import Order, Purchase, Customer, Supplier, Product
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        label = {
            'Product':'Produk', 
        }

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
    
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'