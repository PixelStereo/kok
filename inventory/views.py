#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    """ Exemple de page HTML, non valide pour que l'exemple soit concis """

    text = """<h1>Bienvenue dans l'inventaire Koi Ou Kou (aka KoK)  !</h1>

              <p>Allez, on se prépare !!</p>"""

    return HttpResponse(text)