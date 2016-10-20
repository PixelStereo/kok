from django import forms

from .models import Item, Location, Person

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ()

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ()

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ()
