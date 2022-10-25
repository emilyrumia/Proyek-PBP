
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from general_user.forms import RegisterForm, RekeningBankForm
from general_user.models import GeneralUser
# Create your views here.

def homepage(request):
    return render(request, "general_user/home.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('general_user:homepage'))
        else:
            messages.info(request, 'Email atau password tidak valid.')

    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "general_user/login.html", context)

def register(request):
    form = RegisterForm()
    form_bank = RekeningBankForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        form_bank = RekeningBankForm(request.POST)
        if form.is_valid() and form_bank.is_valid():
            user = form.save()
            rekening_bank = form_bank.save()
            GeneralUser.objects.create(user=user, akun_bank=rekening_bank, no_ponsel=form.cleaned_data.get('no_ponsel'))
            
            login(request, user)

            return redirect('general_user:homepage')
        else:
            print(form_bank.errors)
            
    context = {"form": form, "form_bank": form_bank}
    return render(request, "general_user/register.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('general_user:homepage'))