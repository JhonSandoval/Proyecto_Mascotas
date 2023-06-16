"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

app_name = "app"
urlpatterns = [
    path('', views.index),
    path('index2', views.index_2), 

    path('lists_persons', views.lists_persons, name='listado_personas'), 
    path('lists_persons_json', views.lists_persons_json), 
    path('person/<int:id>', views.detail_person, name='persona-detail'), 
    path('person/<int:id>/mascotas', views.detail_person_mascota, name='persona-detail-mascotas'), 
    
    path('lists_pets', views.lists_pets, name='listado_pets'), 
    path('pet/<str:name>', views.detail_pet), 
    path('pet/<str:name>/observation', views.detail_pet_observation), 
    
    path('specie/<int:id>', views.detail_specie), 
]
