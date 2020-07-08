from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Carsforsale


# Create your views here.


class CarsListView(ListView):
    model = Carsforsale
    template_name = 'carsforsale/cars.html'
    context_object_name = 'cars'
    ordering = ['-date']


class CarCreateView(CreateView):
    model = Carsforsale
    template_name= 'carsforsale/car_upload.html'
    fields = ['title',
              'car_picture',
              'price',
              'make',
              'model',
              'manufactured',
              'mileage',
              'transmission',
              'fuel_type',
              'color',
              'car_description',
              'city',
              'province',
              'phone',
              'email'
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Carsforsale
    template_name = 'carsforsale/car_info.html'


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


def login(request):
    return render(request, 'forms/login_form.html')
