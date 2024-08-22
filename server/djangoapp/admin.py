from django.contrib import admin
from .models import CarMake, CarModel

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)  

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name')
    ordering = ('-year',)  

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)

