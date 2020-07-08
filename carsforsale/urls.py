from django.conf.urls import url
from django.urls import path
from .views import CarsListView, CarDetailView, CarCreateView
from . import views


urlpatterns = [
    url(r'^$', CarsListView.as_view(), name='cars'),
    path('car_information/<int:pk>', CarDetailView.as_view()),
    path('postcar/', CarCreateView.as_view()),
    url(r'^search/$', views.search),
]