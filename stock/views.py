from django.shortcuts import render, redirect
from django.db.models import F
from .models import *
from .forms import OrderForm, PurchaseForm, SupplierForm, CustomerForm, ProductForm, CreateUserForm
from .filters import OrderFilter, PurchaseFilter, ProductFilter

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import plotly.graph_objects as go

def register_view(request):
    if request.user.is_authenticated :
        return redirect('home')
    else :
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Akun ' + user +' berhasil dibuat')

                return redirect('login')

    context = {
        'form' : form
    }
    return render(request, 'stock/register.html', context)

def login_view(request):
    if request.user.is_authenticated :
        return redirect('home')
    else :
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else :
                messages.info(request, 'Username atau password salah')
        context = {}
        return render(request, 'stock/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home_view(request):
    products = Product.objects.all()
    filters = ProductFilter(request.GET, queryset=products)
    products = filters.qs
    context = {
        'filter' : filters,
        'products' : products
    }
    return render(request, 'stock/home.html', context)

@login_required(login_url='login')
def order_view(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()


    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    filter_order = OrderFilter(request.GET, queryset=orders)
    orders = filter_order.qs

    

    context = {
        'filter' : filter_order,
        'customers' : customers,
        'orders' : orders,
        'delivered' : delivered,
        'pending' : pending,
        'total_orders' : total_orders,
    }

    return render(request, 'stock/order.html', context)

@login_required(login_url='login')
def purchase_view(request):
    suppliers = Supplier.objects.all()
    purchases = Purchase.objects.all()
    total_purchases = purchases.count()
    arrived = purchases.filter(status='Arrived').count()
    pending = purchases.filter(status='Pending').count()

    filter_purchase = PurchaseFilter(request.GET, queryset=purchases)
    purchases = filter_purchase.qs

    

    context = {
        'filter' : filter_purchase,
        'suppliers' : suppliers,
        'purchases' : purchases,
        'arrived' : arrived,
        'pending' : pending,
        'total_purchases' : total_purchases
    }

    return render(request, 'stock/purchase.html', context)

#order CUD
@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST': 
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            product_order = request.POST['product']
            order_quantity = request.POST['quantity']
            product = Product.objects.get(id=product_order)
            product.quantity = F('quantity') - order_quantity
            product.save()  
            return redirect('/order')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/order')
    context = {
        'item' : order
    }
    return render(request, 'stock/delete.html', context)

#purchase CUD
@login_required(login_url='login')
def createPurchase(request):
    form = PurchaseForm()
    if request.method == 'POST': 
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            product_order = request.POST['product']
            order_quantity = request.POST['quantity']
            product = Product.objects.get(id=product_order)
            product.quantity = F('quantity') + order_quantity
            product.save()
            return redirect('/purchase')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deletePurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    if request.method == "POST":
        purchase.delete()
        return redirect('/purchase')
    context = {
        'item' : purchase
    }
    return render(request, 'stock/delete.html', context)

#customer CUD
@login_required(login_url='login')
def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST': 
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/order')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST': 
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/order')
    context = {
        'form' : form,
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('/order')
    context = {
        'item' : customer
    }
    return render(request, 'stock/delete.html', context)

#supplier CUD
@login_required(login_url='login')
def createSupplier(request):
    form = SupplierForm()
    if request.method == 'POST': 
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/purchase')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
def updateSupplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    form = SupplierForm(instance=supplier)
    if request.method == 'POST': 
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('/purchase')
    context = {
        'form' : form,
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
def deleteSupplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    if request.method == "POST":
        supplier.delete()
        return redirect('/order')
    context = {
        'item' : supplier
    }
    return render(request, 'stock/delete.html', context)


#product CUD
@login_required(login_url='login')
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST': 
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST': 
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form,
    }
    return render(request, 'stock/form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/order')
    context = {
        'item' : product
    }
    return render(request, 'stock/delete.html', context)

@login_required(login_url='login')
def viewPhoto(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'stock/photo.html', context)


def viewReport(request):
    product = Product.objects.all()
    purchase = Purchase.objects.all()
    order = Order.objects.all()
    x_product = []
    y_product = []

    
    for i in product: 
        x_product.append(i.name)
        y_product.append(i.quantity)
    fig_prod = go.Figure(go.Bar(
        x=x_product,
        y=y_product,
        orientation='v',
        hovertemplate='<br>%{y}%'
    ))
    fig_prod.update_yaxes(title='Kuantitas')
    fig_prod.update_xaxes(title='Produk')

    x_order = []
    y_order = []
    for i in order: 
        x_order.append(i.product.name)
        y_order.append(i.total)
    fig_order = go.Figure(go.Bar(
        x=x_order,
        y=y_order,
        orientation='v',
        hovertemplate='<br>%{y}%'
    ))
    fig_order.update_yaxes(title='Total Transaksi (Pemesanan)')
    fig_order.update_xaxes(title='Produk')


    x_purchase = []
    y_purchase = []
    for i in purchase: 
        x_purchase.append(i.product.name)
        y_purchase.append(i.total)
    fig_purchase = go.Figure(go.Bar(
        x=x_purchase,
        y=y_purchase,
        orientation='v',
        hovertemplate='<br>%{y}%'
    ))
    fig_purchase.update_yaxes(title='Total Transaksi (Pembelian Stok)')
    fig_purchase.update_xaxes(title='Produk')


    context = {
        'fig_prod' : fig_prod.to_html,
        'fig_order' : fig_order.to_html,
        'fig_purchase' : fig_purchase.to_html
    }
    return render(request, 'stock/report.html', context)