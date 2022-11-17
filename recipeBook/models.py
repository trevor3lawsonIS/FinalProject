from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Recipe_Class(models.Model):
  RecipeClassDescription = models.CharField(max_length=30)

  def __str__(self):
    return (self.RecipeClassDescription)

class Recipe(models.Model):
    RecipeTitle = models.CharField(max_length=50)
    Preparation = models.TextField
    Notes = models.TextField
    RecipeClassID = models.ForeignKey(Recipe_Class, on_delete=models.CASCADE)
    def __str__(self):
        return (self.RecipeTitle)

class Ingredient_Class(models.Model):
                IngredientClassDescription = models.CharField(max_length=30)
                def __str__(self):
                    return (self.IngredientClassDescription)

class Ingredient(models.Model):
    IngredientName = models.CharField(max_length=20)
    IngredientClassID = models.ForeignKey(Ingredient_Class, on_delete=models.CASCADE)

    def __str__(self):
        return (self.IngredientName)

class Recipe_Ingredient(models.Model):
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    Amount = models.CharField(max_length=20)

    def __str__(self) :
        return (self.Amount)