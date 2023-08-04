from .import views
from django .urls import path
from .views import *
urlpatterns = [
    path('', VehicleList.as_view(), name='vehicle_list'),

  

  ]
