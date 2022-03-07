# Generated by Django 3.2.9 on 2021-12-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20211217_1532'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredientrecipe',
            constraint=models.UniqueConstraint(fields=('ingredient', 'recipe', 'amount'), name='unique_ingredient_recipe'),
        ),
        migrations.AddConstraint(
            model_name='shopingcart',
            constraint=models.UniqueConstraint(fields=('customer', 'cart'), name='unique_cart'),
        ),
    ]
