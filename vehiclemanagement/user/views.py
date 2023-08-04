from django.shortcuts import render
from super_admin .models import Vehicle
from django.views.generic import ListView
# Create your views here.


class VehicleList(ListView):
    model = Vehicle
    template_name = 'vehicles_list.html'
    context_object_name = 'vehicles'