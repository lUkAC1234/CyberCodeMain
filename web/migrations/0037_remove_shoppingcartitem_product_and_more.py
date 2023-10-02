# Generated by Django 4.2.3 on 2023-10-02 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0036_remove_shoppingcartitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='shoppingcartitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.pricingmodel'),
        ),
    ]
