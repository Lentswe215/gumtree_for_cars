from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cars, name='cars'),
    url(r'^car_information/(?P<id>\d+)$', views.carInfo),
    url(r'^search/$', views.search)
]