# Generated by Django 4.2.3 on 2023-10-02 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_remove_shoppingcartitem_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.pricingmodel'),
        ),
    ]
