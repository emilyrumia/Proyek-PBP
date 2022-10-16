from django.shortcuts import redirect, render
from django.http import HttpResponse
from general_user.forms import GeneralUserRegisterForm

# Create your views here.
def homepage(request):
    return render(request, "general_user/home.html")

def login(request):
    return render(request, "general_user/login.html")

def register(request):
    form = GeneralUserRegisterForm()
    if request.method == "POST":
        form = GeneralUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general_user:login')
    
    context = {'form':form}
    return render(request, "general_user/register.html", context)