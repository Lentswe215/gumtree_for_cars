from django.db import models
from datetime import datetime


# Create your models here.
class Carsforsale(models.Model):
    transmission_choices = (
        ('Automatic', 'Automatic'), ('Manual', 'Manual')
    )
    fuel_choices = (
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol')
    )
    provinces = (
        ('Gauteng', 'Gauteng'),
        ('North West', 'North west'),
        ('Free State', 'Free State'),
        ('Western Cape', 'Western Cape'),
        ('Mpumalanga', 'Mpumalanga'),
        ('Limpopo', 'Limpopo'),
        ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'),
        ('KwaZulu Natal', 'KwaZulu Natal'),

    )
    title = models.CharField(default='', max_length= 100)
    date = models.DateField(default= datetime.now, blank=True)
    car_picture = models.ImageField(upload_to='cars_pictures', blank=True)
    price = models.CharField(default=0, max_length= 10) 
    make = models.CharField(max_length= 50, default='')
    model = models.CharField(max_length= 50, default='')
    manufactured = models.CharField(max_length=4, default='')
    mileage = models.CharField(max_length= 10, default=0)
    transmission = models.CharField(default='', max_length=20, choices= transmission_choices)
    fuel_type = models.CharField(default='', max_length= 10, choices=fuel_choices)
    color =  models.CharField(default='', max_length= 50)
    car_description = models.TextField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50, choices= provinces)
    phone = models.CharField(max_length=10, default=0)
    email = models.EmailField(default='example@gmail.com', max_length= 50)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Carsforsale'




