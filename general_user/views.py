from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from general_user.forms import GeneralUserRegisterForm

# Create your views here.
def homepage(request):
    return render(request, "general_user/home.html")

def login_user(request):
    return render(request, "general_user/login.html")

def register(request):
    form = GeneralUserRegisterForm()
    if request.method == "POST":
        form = GeneralUserRegisterForm(request.POST)
        if form.is_valid():
            general_user = form.save()
            login(request, general_user)
            return redirect('general_user:homepage')
    
    context = {'form':form}
    return render(request, "general_user/register.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('general_user:homepage'))