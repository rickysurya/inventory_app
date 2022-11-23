from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('order/', order_view, name="order"),
    path('purchase/', purchase_view, name="purchase"),
    path('create_order/', createOrder, name="create_order"),
    path('update_order/<int:pk>/', updateOrder, name="update_order"),
    path('delete_order/<int:pk>/', deleteOrder, name="delete_order"),
    path('create_purchase/', createPurchase, name="create_purchase"),
    path('update_purchase/<int:pk>/', updatePurchase, name="update_purchase"),
    path('delete_purchase/<int:pk>/', deletePurchase, name="delete_purchase"),

]