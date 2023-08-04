from .import views
from django .urls import path
from .views import *
urlpatterns = [
  path('', VehicleList.as_view(), name='management_vehicle_list'),
  path('<int:pk>/update/', VehicleUpdate.as_view(), name='update_vehicle'),
  

  ]
