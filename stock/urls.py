from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', home_view, name="home"),
    path('order/', order_view, name="order"),
    path('purchase/', purchase_view, name="purchase"),
    
    path('create_order/', createOrder, name="create_order"),
    path('update_order/<int:pk>/', updateOrder, name="update_order"),
    path('delete_order/<int:pk>/', deleteOrder, name="delete_order"),

    path('create_purchase/', createPurchase, name="create_purchase"),
    path('update_purchase/<int:pk>/', updatePurchase, name="update_purchase"),
    path('delete_purchase/<int:pk>/', deletePurchase, name="delete_purchase"),

    path('create_customer/', createCustomer, name="create_customer"),
    path('update_customer/<int:pk>/', updateCustomer, name="update_customer"),
    path('delete_customer/<int:pk>/', deleteCustomer, name="delete_customer"),

    path('create_supplier/', createSupplier, name="create_supplier"),
    path('update_supplier/<int:pk>/', updateSupplier, name="update_supplier"),
    path('delete_supplier/<int:pk>/', deleteSupplier, name="delete_supplier"),

    path('create_product/', createProduct, name="create_product"),
    path('update_product/<int:pk>/', updateProduct, name="update_product"),
    path('delete_product/<int:pk>/', deleteProduct, name="delete_product"),
    path('photo/<int:pk>/', viewPhoto, name="view_photo"),
    path('report/', viewReport, name='report')

]