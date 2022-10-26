
from testimoni.models import testimoniList

from django.core import serializers
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# Method untuk menampilkan testimoni dari semua pengguna
def show_testimoni(request) :   
    # Menampilkan semua testimoni (maupun bagi yang belum login)
    list_testimoni = testimoniList.objects.all()

    context = {
        'list_testimoni' : list_testimoni
    }

    return render(request, "testimoni.html", context)

def show_testimoni_json(request):
    listTestimoni = testimoniList.objects.all()
    return HttpResponse(serializers.serialize('json', listTestimoni), content_type="application/json")


# Method untuk menambahkan testimoni (dibutuhkan login akun)
@login_required(login_url='/login')
def add_testimoni(request) :
    if request.method == "POST" :
        user_logged_in = request.user
        nama = request.POST.get("nama")
        pesan = request.POST.get("pesan")

        testimoniBaru = testimoniList(user=user_logged_in, nama=nama, pesan=pesan)
        testimoniBaru.save()
        return HttpResponse(status=200)
    return redirect("testimoni:tampilan_testimoni")