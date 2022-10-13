from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "home.html")

def login(request):
    return HttpResponse("Ini halaman login")

def register(request):
    return HttpResponse("Ini halaman register")