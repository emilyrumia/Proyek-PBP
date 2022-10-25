from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# Method untuk menampilkan testimoni dari semua pengguna
def show_testimoni(request) :
    return HttpResponse("Ini testimoni pengguna")

# Method untuk menambahkan testimoni (dibutuhkan login akun)
@login_required(login_url='/login')
def add_testimoni(request) :
    return  