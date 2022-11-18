from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Recipe_Class(models.Model):
  RecipeClassDescription = models.CharField(max_length=30)

  def __str__(self):
    return (str(self.id))

class Recipe(models.Model):
    RecipeTitle = models.CharField(max_length=50)
    Preparation = models.CharField(max_length=2000)
    Notes = models.CharField(max_length=2000)
    RecipeClassID = models.ForeignKey(Recipe_Class, on_delete=models.CASCADE)

    def __str__(self):
        return (self.RecipeTitle)

class Ingredient(models.Model):
    IngredientName = models.CharField(max_length=20)

    RecipeID = models.ManyToManyField('Recipe', through='Recipe_Ingredient')

    def __str__(self):
        return (self.IngredientName)

class Recipe_Ingredient(models.Model):
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    Amount = models.CharField(max_length=20)

    def __str__(self) :
        return (self.Amount)