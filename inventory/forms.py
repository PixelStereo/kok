from django import forms

from .models import Item

class PostForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'serial', 'description', 'purchase_date', 'purchase_price', 'notes', )
