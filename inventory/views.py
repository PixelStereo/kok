#-*- coding: utf-8 -*-

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, Http404

def home(request):

    """
    Home page
    """

    text = """<h1>Bienvenue dans l'inventaire Koi Ou Kou (aka KoK)  !</h1>

              <p>Allez, on se prépare !!</p>"""

    return HttpResponse(text)

def view_item(request, id_item):
    """
	View of an item
	"""
    if int(id_item) > 100:
        raise Http404
    text = "<h1>This is the view of the item " + id_item + " </h1>"
    return HttpResponse(text)

def list_items(request):
    """
	View of a list of items
	no arguments give the list of all items
	arguments will filter values (per location, per price etc…)
	"""
    return HttpResponse(answer)

def date_actuelle(request):
    """
	return the date
	"""
    return render(request, 'inventory/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):    
    """
	make an addition
	"""
    total = int(nombre1) + int(nombre2)
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'inventory/addition.html', locals())
