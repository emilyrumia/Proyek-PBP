from lib2to3.pgen2.token import GREATER
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    if not request.user.is_authenticated:
        return redirect('general_user:homepage')
    else:
        return render(request, "resipien/home.html")