from django.contrib import admin

from .models import Item, ItemAdmin, Location, LocationAdmin, Person


admin.site.register(Location, LocationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Person)