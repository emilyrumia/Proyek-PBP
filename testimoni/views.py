import random
from general_user.models import GeneralUser
from testimoni.models import TestimoniList

from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Method untuk menampilkan testimoni dari semua pengguna
def show_testimoni(request) :   
    # Menampilkan semua testimoni (maupun bagi yang belum login)
    list_testimoni = TestimoniList.objects.all()

    initiate_list_testimoni = list(TestimoniList.objects.all()) 
    random_testimoni = random.sample(initiate_list_testimoni, 3)
    first_random_testimoni = random_testimoni[0]
    second_random_testimoni = random_testimoni[1]
    third_random_testimoni = random_testimoni[2]

    context = {
        'list_testimoni' : list_testimoni,
        'first_random_testimoni' : first_random_testimoni,
        'second_random_testimoni' : second_random_testimoni,
        'third_random_testimoni' : third_random_testimoni
    }

    return render(request, "testimoni.html", context)

# Method untuk menampilkan data testimoni dengan format json
def show_testimoni_json(request):
    list_testimoni = TestimoniList.objects.all()
    return HttpResponse(serializers.serialize('json', list_testimoni), content_type="application/json")


def show_random_testimoni(request):
    list_testimoni = list(TestimoniList.objects.all())
    random_testimoni = random.sample(list_testimoni, 3)
    
    return HttpResponse(serializers.serialize('json', random_testimoni), content_type="application/json")

# Method untuk menambahkan testimoni (dibutuhkan login akun)
@login_required(login_url='/login')
def add_testimoni(request) :
    if request.method == "POST" :
        user_logged_in = GeneralUser.objects.get(user=request.user)
        nama = request.POST.get("nama")
        title = request.POST.get("title")
        target = request.POST.get("target")
        pesan = request.POST.get("pesan")

        if len(nama) == 0 :
            nama = "Anonymous"

        if len(target) == 0 :
            target = "-"

        testimoni_baru = TestimoniList(user=user_logged_in, nama=nama, title=title, target=target, pesan=pesan)
        testimoni_baru.save()

        return redirect("testimoni:show_testimoni")
    return HttpResponseNotFound()
