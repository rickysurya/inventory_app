# Generated by Django 4.1.3 on 2022-11-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_remove_order_price_remove_purchase_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]