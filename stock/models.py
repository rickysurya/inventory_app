from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='Nama Produk',max_length=200, null=False)
    quantity = models.IntegerField(verbose_name='Kuantitas',default=0)
    image = models.ImageField(null=True)

    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(verbose_name='Nama Pelanggan',max_length=200, null=True)
    phone = models.CharField(verbose_name='Telp.',max_length=200, null=True)
    email = models.EmailField(verbose_name='Email')
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(verbose_name='Nama Pemasok',max_length=200, null=True)
    phone = models.CharField(verbose_name='Telp.',max_length=200, null=True)
    email = models.EmailField(verbose_name='Email')
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    product = models.ForeignKey(Product, verbose_name='Nama Produk',null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, verbose_name='Nama Pelanggan', null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(verbose_name='Kuantitas', default=0)
    price = models.DecimalField(verbose_name='Harga', default=0, decimal_places=0, max_digits=10)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(verbose_name='Status',max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name

    @property
    def total(self):
        return self.quantity * self.price

class Purchase(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Arrived', 'Arrived'),
    )
    product = models.ForeignKey(Product, verbose_name='Nama Produk', null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, verbose_name='Nama Pemasok', null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(verbose_name='Kuantitas', default=0)
    price = models.DecimalField(verbose_name='Harga', default=0, decimal_places=0, max_digits=10)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(verbose_name='Status',max_length=100, null=True, choices=STATUS)
    

    def __str__(self):
        return self.product.name

    @property
    def total(self):
        return self.quantity * self.price