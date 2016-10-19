from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    serial = models.TextField(null=True)
    purchase_date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date d'achat")
    purchase_price = models.CharField(max_length=9, verbose_name="Prix d'achat")
    location = models.ForeignKey('Location', null=True)

    def __str__(self):
        """
    	representation as a string
    	"""
        return 'Item (name:{name}, description:{description}, serial:{serial}, \
                purchase_date:{purchase_date}, purchase_price:{purchase_price}'
        item.format(name=self.name, description=self.description, serial=self.serial, \
                    purchase_date=self.purchase_date, purchase_price=self.purchase_price)

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    contact = models.TextField(null=True)

    def __str__(self):
        """
    	representation as a string
    	"""
        return 'Item (name:{name}, description:{description}, address:{address}, contact:{contact}'
        item.format(name=self.name, description=self.description, \
                    address=self.address, contact=self.contact)