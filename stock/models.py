from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    quantity = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name

class Purchase(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Arrived', 'Arrived'),
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name