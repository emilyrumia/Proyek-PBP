from lib2to3.pgen2.token import GREATER
from django.shortcuts import redirect, render
from django.http import HttpResponse
from general_user.models import GeneralUser

# Create your views here.
def homepage(request):
    if not request.user.is_authenticated or not isinstance(request.user, GeneralUser):
        return redirect('general_user:homepage')
    else:
        return render(request, "resipien/home.html")