from .import views
from django .urls import path
from .views import *
urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('', LogView.as_view(), name='login'),
  path('logout/', LogoutUserView.as_view(), name='logout'),


  

  ]