from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

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

    status_choices = (
        ('available', 'available'),
        ('sold','sold')
    )

    title = models.CharField(default='', max_length= 100)
    date = models.DateField(default= datetime.now, blank=True)
    car_picture = models.ImageField(upload_to='cars_pictures', default='noimage.jpg', blank=True)
    price = models.CharField(default=0, max_length= 10) 
    status = models.CharField(max_length=10, default='avalable', choices= status_choices)
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
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default=0)
    email = models.EmailField(default='example@gmail.com', max_length= 50)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('car_info', kwargs={'pk': self.pk})


    class Meta:
        verbose_name_plural = 'Carsforsale'




