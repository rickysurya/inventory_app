# Generated by Django 4.1.3 on 2022-11-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_customer_date_created_supplier_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
