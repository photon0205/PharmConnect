# Generated by Django 5.0.4 on 2024-04-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_remove_inventory_store_product_store"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="total_sold_quantity",
            field=models.IntegerField(default=0),
        ),
    ]
