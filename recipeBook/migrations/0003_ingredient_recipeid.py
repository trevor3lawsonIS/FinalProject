# Generated by Django 4.1.2 on 2022-11-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeBook', '0002_remove_ingredient_ingredientclassid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='RecipeID',
            field=models.ManyToManyField(through='recipeBook.Recipe_Ingredient', to='recipeBook.recipe'),
        ),
    ]