from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, PurchaseForm

# Create your views here.
def home_view(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'stock/home.html', context)

def order_view(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'customers' : customers,
        'orders' : orders,
        'delivered' : delivered,
        'pending' : pending,
        'total_orders' : total_orders,
    }

    return render(request, 'stock/order.html', context)

def purchase_view(request):
    suppliers = Supplier.objects.all()
    purchases = Purchase.objects.all()
    total_purchases = purchases.count()
    arrived = purchases.filter(status='Arrived').count()
    pending = purchases.filter(status='Pending').count()

    context = {
        'suppliers' : suppliers,
        'purchases' : purchases,
        'arrived' : arrived,
        'pending' : pending,
        'total_purchases' : total_purchases
    }

    return render(request, 'stock/purchase.html', context)

#order CUD
def createOrder(request):
    form = PurchaseForm()
    if request.method == 'POST': 
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST': 
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
                form.save()
                return redirect('/order')
    context = {
        'form' : form,
    }
    return render(request, 'stock/form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/order')
    context = {
        'order' : order
    }
    return render(request, 'stock/delete.html', context)

#purchase CUD
def createPurchase(request):
    form = PurchaseForm()
    if request.method == 'POST': 
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/purchase')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

def updatePurchase(request, pk):

    purchase = Purchase.objects.get(id=pk)
    form = PurchaseForm(instance=purchase)
    if request.method == 'POST': 
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
                form.save()
                return redirect('/purchase')
    context = {
        'form' : form,
    }
    return render(request, 'stock/form.html', context)

def deletePurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    if request.method == "POST":
        purchase.delete()
        return redirect('/order')
    context = {
        'purchase' : purchase
    }
    return render(request, 'stock/delete.html', context)

#customer CUD
def createCustomer(request):
    form = PurchaseForm()
    if request.method == 'POST': 
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/purchase')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

def updatePurchase(request, pk):

    purchase = Purchase.objects.get(id=pk)
    form = PurchaseForm(instance=purchase)
    if request.method == 'POST': 
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
                form.save()
                return redirect('/purchase')
    context = {
        'form' : form,
    }
    return render(request, 'stock/form.html', context)

def deletePurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    if request.method == "POST":
        purchase.delete()
        return redirect('/order')
    context = {
        'purchase' : purchase
    }
    return render(request, 'stock/delete.html', context)

#supplier CUD
