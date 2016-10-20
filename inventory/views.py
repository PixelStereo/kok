#-*- coding: utf-8 -*-

from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Item, Location, Person
from .forms import ItemForm, LocationForm, PersonForm

def home(request):

    """
    Home page
    """
    return render(request, 'inventory/home.html')

def view_item(request, id_item):
    """
    View of an item
    """
    item = get_object_or_404(Item, id=id_item)
    return render(request, 'inventory/item.html', {item: item})

def new_item(request):
    """
    create a new item
    """
    item = ItemForm()
    if item.is_valid():
        item.save()
    return render(request, 'inventory/new-item.html', {'item': item})

def list_items(request):
    """
    View of a list of items
    no arguments give the list of all items
    arguments will filter values (per location, per price etc…)
    """
    # list all items
    items = Item.objects.all()
    return render(request, 'inventory/items.html', {'items': items})

def view_location(request, id_location):
    """
    View of an item
    """
    location = get_object_or_404(Location, id=id_location)
    return render(request, 'inventory/location.html', {location: location})

def new_location(request):
    """
    create a new item
    """
    location = LocationForm()
    if location.is_valid():
        location.save()
    return render(request, 'inventory/new-location.html', {'location': location})

def list_locations(request):
    """
    View of a list of location
    no arguments give the list of all locations
    arguments will filter values (per person, per item etc…)
    """
    # list all items
    locations = Location.objects.all()
    return render(request, 'inventory/locations.html', {'locations': locations})

def view_person(request, id_person):
    """
    View of a person
    """
    person = get_object_or_404(Person, id=id_person)
    return render(request, 'inventory/person.html', {person: person})

def new_person(request):
    """
    create a new item
    """
    person = PersonForm()
    if person.is_valid():
        person.save()
    return render(request, 'inventory/new-person.html', {'person': person})

def list_persons(request):
    """
    View of a list of items
    no arguments give the list of all items
    arguments will filter values (per location, per price etc…)
    """
    # list all items
    persons = Person.objects.all()
    return render(request, 'inventory/persons.html', {'persons': persons})

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

def clear(request):
    for item in Item.objects.all():
        item.delete()
    return HttpResponse('all items have been removed')
