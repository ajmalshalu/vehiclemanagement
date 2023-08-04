from django.shortcuts import render
from super_admin.models import Vehicle
from django.views.generic import ListView,UpdateView
from django.urls import reverse_lazy

# Create your views here.


class VehicleList(ListView):
    model = Vehicle
    template_name = 'vehiclelist.html'
    context_object_name = 'vehicles'


class VehicleUpdate(UpdateView):
    model = Vehicle
    template_name = 'update_detail.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('management_vehicle_list')