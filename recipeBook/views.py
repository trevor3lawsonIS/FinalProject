from django.shortcuts import render
from django.http import HttpResponse
from recipeBook.models import Ingredient, Recipe_Ingredient, Recipe, Recipe_Class

# Create your views here.
def indexPageView(request) :
    data = Recipe.objects.all()

    context = {
        'rec': data
    }
    return render(request, 'recipeBook/index.html', context) 

def createPageView(request) :
    return render(request, 'recipeBook/create.html')

def updatePageView(request) :
    return render(request, 'recipeBook/update.html')

def readPageView(request, rec_id) :
    recipeData = Recipe.objects.get(id = rec_id)
    # ingredientData = Ingredient.objects.get(recipeID = rec_id)
    # amountData = Recipe_Ingredient.objects.get(recipeID = rec_id)
    context = {
        'rec': recipeData,
        # 'ing': ingredientData,
        # 'amt': amountData
    }
    return render(request, 'recipeBook/read.html', context) 

# Delete
def deleteRecipePageView(request, rec_id):
    data = Recipe.objects.get(id = rec_id)

    data.delete()

    return indexPageView(request)