from django.conf.urls import url
from django.urls import path
from .views import CarsListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView
from . import views


urlpatterns = [
    url(r'^$', CarsListView.as_view(), name='cars'),
    path('car_information/<int:pk>/', CarDetailView.as_view(), name = 'car_info'),
    path('postcar/', CarCreateView.as_view(), name= 'create_car'),
    path('updatecar/<int:pk>/', CarUpdateView.as_view(), name= 'update_car'),
    path('deletecar/<int:pk>/', CarDeleteView.as_view(), name= 'delete_car'),
    url(r'^search/$', views.search),
]