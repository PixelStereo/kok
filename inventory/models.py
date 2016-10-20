#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    serial = models.CharField(max_length=100, null=True)
    purchase_date = models.DateTimeField(auto_now=False, 
                                verbose_name="Date d'achat", default=timezone.now)
    purchase_price = models.CharField(max_length=9, verbose_name="Prix d'achat")
    location = models.ForeignKey('Location', null=True)

    def __str__(self):
        """
    	representation as a string
    	"""
    	return self.name

class ItemAdmin(admin.ModelAdmin):
    #list_display = ('name', 'description', 'purchase_date', 'location')
    list_filter = ('name','purchase_date', 'location')
    date_hierarchy = 'purchase_date'
    ordering = ('name', 'purchase_date')
    search_fields = ('name', 'description', 'purchase_date', 'location')
    fields = ('name', 'description', 'serial', 'purchase_date', 'purchase_price', 'location')

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    address = models.CharField(max_length=400)
    contact = models.ForeignKey('Person', null=True)

    def __str__(self):
        """
    	representation as a string
    	"""
        return self.name

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'contact')
    list_filter = ('name','address', 'contact')
    ordering = ('name', 'address')
    search_fields = ('name', 'description', 'address', 'contact')
    fields = ('name', 'description', 'address', 'contact')

class Person(models.Model):
    firstname = models.CharField(max_length=100, verbose_name="First Name")
    lastname = models.CharField(max_length=100, verbose_name="Last Name")
    phone = models.CharField(max_length=400, verbose_name="Phone Number")
    mail = models.EmailField(verbose_name="Email address")

    def __str__(self):
        """
        representation as a string
        """
        return self.firstname + ' ' + self.lastname