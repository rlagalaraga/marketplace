# Generated by Django 4.1.5 on 2023-02-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]
