# Generated by Django 4.2.3 on 2023-10-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0035_shoppingcartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='shoppingcartitem',
            name='product',
            field=models.ManyToManyField(to='web.pricingmodel'),
        ),
    ]