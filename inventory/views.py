#-*- coding: utf-8 -*-

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Item

def home(request):

    """
    Home page
    """
    return render(request, 'inventory/home.html')

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
    # list all items
    items = Item.objects.all()
    return render(request, 'inventory/items.html', {'items': items})

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

def hello(request, name):
    """
    say hello to the user
    """
    return render(request, 'inventory/hello.html', {'date': datetime.now(), 'name': name.capitalize()})

def rainbow(request):
    """
    colors of a rainbow
    """
    couleurs = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
    return render(request, 'inventory/rainbow.html', {'couleurs': couleurs})

def new_item(request):
    """
    create a new item
    """
    item = Item(name='item without name')
    item.save()
    return render(request, 'inventory/item.html', {'item': item})

def clear(request):
    for item in Item.objects.all():
        item.delete()
    return HttpResponse('all items have been removed')
