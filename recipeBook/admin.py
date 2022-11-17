from django.contrib import admin
from .models import Ingredient, Recipe, Ingredient_Class, Recipe_Ingredient, Recipe_Class

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe_Class)
admin.site.register(Recipe)
admin.site.register(Ingredient_Class)
admin.site.register(Recipe_Ingredient)