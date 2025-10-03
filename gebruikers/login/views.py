from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
    path('login/', include('gebruiker.urls'))
]

