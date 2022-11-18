from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'recipeBook/index.html') 

def createPageView(request) :
    return render(request, 'recipeBook/create.html')

def updatePageView(request) :
    return render(request, 'recipeBook/update.html')

def readPageView(request) :
    return render(request, 'recipeBook/read.html') 