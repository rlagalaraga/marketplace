# Generated by Django 4.1.5 on 2023-01-24 20:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=80, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=80, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')]),
        ),
    ]
