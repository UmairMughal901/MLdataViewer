from django.contrib import admin
from django.urls import path
from mapviewer import views

urlpatterns = [
    path("", views.index, name='mapviewer'),
    path("map2", views.map2, name='map2')
    
]