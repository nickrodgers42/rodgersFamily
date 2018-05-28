from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
import json

def index(request):
    conn = psycopg2.connect("dbname=rodgersfamily user=nrodgers password=lazeratz")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT section FROM recipes ORDER BY section ASC;")
    subSections = cur.fetchall() 
    context={
    }
    return render(request, 'recipes/index.html', context) 

def getSubsections(request):
    if 'section' in request.GET:
        section = request.GET['section']
    conn = psycopg2.connect("dbname=rodgersfamily user=postgres password=postgres")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT section FROM recipes ORDER BY section ASC;")
    subSections = cur.fetchall()
    resp = {
        'subSections': subSections
    }
    return HttpResponse(json.dumps(resp))

def recipe(request, recipe_id):
    conn = psycopg2.connect("dbname=rodgersfamily user=nrodgers password=lazercatz")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT section FROM recipes ORDER BY section ASC;")
    subSections = cur.fetchall() 
    context={
        'subSections': subSections
    }
    return render(request, 'recipes/recipe.html', context)
