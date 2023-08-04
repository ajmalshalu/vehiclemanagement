from .import views
from django .urls import path
from .views import *
urlpatterns = [
  path('', VehicleListView.as_view(), name='super_vehicle_list'),
  path('addvehicle/', VehicleCreateView.as_view(), name='add_vehicle'),
  path('<int:pk>/update/', VehicleUpdateView.as_view(), name='update_vehicle'),
  path('<int:pk>/delete/', VehicleDeleteView.as_view(), name='delete_vehicle'),
  

  ]
