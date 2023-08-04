from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import CustUser
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView,FormView

# Create your views here.
class LogView(FormView):
    template_name="registration/login.html"
    form_class=LogForm
    def post(self,request):
        form=LogForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pswd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                if user.user_type=="super_admin":
                    login(request,user)
                    return redirect('super_vehicle_list')
                elif user.user_type=="management_admin":
                    login(request,user)
                    return redirect('management_vehicle_list')
            else:
                return render(request,"login.html",{"form":form})
        else:
                return render(request,"login.html",{"form":form})


class RegisterView(CreateView):
    model = CustUser
    form_class = RegForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class LogoutUserView(LogoutView):
    next_page = 'vehicle_list'