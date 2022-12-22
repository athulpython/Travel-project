from django.contrib import admin
from . models import place,Destination

# Register your models here.
class placeAdmin(admin.ModelAdmin):
    list_display =['name','img','desc','price','offer']
admin.site.register(place)

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'desc']
admin.site.register(Destination)

