from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={}
    return render(request, 'recipes/index.html', context) 

def recipe(request, recipe_id):
    context={}
    return render(request, 'recipes/recipe.html', context)
