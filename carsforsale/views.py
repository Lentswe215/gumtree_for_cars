from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import Carsforsale


# Create your views here.
def cars(request):
    carsAvailable = Carsforsale.objects.order_by('-date')[:20]

    return render(request, 'carsforsale/cars.html', {
        'cars': carsAvailable,
        'pagetitle': 'available cars'
    })


def carInfo(request, id):

    currentCar = Carsforsale.objects.get(id=id)
    return render(request, 'carsforsale/car_info.html', {
        'car': currentCar,
        'pagetitle': currentCar.title
        })

    def __str__(self):
        return self.title


def search(request):
    if request.method == 'POST':
        search_box = request.POST['searchbox']

        if search_box:
            match = Carsforsale.objects.filter(
                Q(make__icontains=search_box) |
                Q(model__icontains=search_box) |
                Q(transmission__icontains=search_box) |
                Q(color__icontains=search_box) |
                Q(city__icontains=search_box) |
                Q(province__icontains=search_box) |
                Q(fuel_type__icontains=search_box)
            )
            if match:
                return render(request, 'carsforsale/search.html', {'cars': match})
            else:
                messages.error(request, 'Match not found')
                return render(request, 'carsforsale/search.html', {
                    'cars': match,
                    'pagetitle': search
                })
    
