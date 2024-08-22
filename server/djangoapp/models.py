from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)  
    founded_year = models.PositiveIntegerField(blank=True, null=True)  
    headquarters_location = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return self.name

class CarModel(models.Model):
    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('COUPE', 'Coupe')
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    dealer_id = models.IntegerField()   
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=CAR_TYPE_CHOICES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    color = models.CharField(max_length=50, blank=True, null=True)  
    engine_size = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)  

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year.year})"