from django.forms import ModelForm
from .models import Order, Purchase, Customer, Supplier

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

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