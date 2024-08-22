from django.contrib import admin
from .models import CarMake, CarModel

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'founded_year', 'headquarters_location')
    search_fields = ('name', 'description')
    list_filter = ('founded_year', 'headquarters_location')
    ordering = ('name',)  

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'type', 'year', 'dealer_id', 'color', 'engine_size')
    list_filter = ('make', 'type', 'year')
    search_fields = ('name', 'make__name', 'dealer_id')
    ordering = ('-year',)  

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)

