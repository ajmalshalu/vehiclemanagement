from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehicle

# Create your views here.

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'create_vehicle.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('super_vehicle_list')

class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'create_vehicle.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('super_vehicle_list')

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    success_url = reverse_lazy('super_vehicle_list')


