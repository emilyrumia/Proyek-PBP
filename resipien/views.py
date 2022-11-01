# from lib2to3.pgen2.token import GREATER
from inspect import stack
import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from general_user.forms import RekeningBankForm
from general_user.models import GeneralUser, RekeningBank
from resipien.models import GalangDana, Komentar
from resipien.forms import GalangForm
from django.contrib import messages
import datetime
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@login_required(login_url='/general_user/login/')
@csrf_protect
def show_buat_galang(request):
    formGalang = GalangForm()
    formBank = RekeningBankForm()
    if request.method == 'POST':
        formGalang = GalangForm(request.POST, request.FILES)
        formBank = RekeningBankForm(request.POST)
        if formGalang.is_valid() & formBank.is_valid():
            user = GeneralUser.objects.get(user=request.user)
            tujuan = formGalang.cleaned_data["tujuan"]
            judul = formGalang.cleaned_data["judul"]
            deskripsi = formGalang.cleaned_data["deskripsi"]
            target = formGalang.cleaned_data["target"]
            gambar = formGalang.cleaned_data["gambar"]
            tanggal_pembuatan = datetime.datetime.now()
            tanggal_berakhir = datetime.datetime.now()
            status_keaktifan = True
            akun_bank = formBank.save()
            GalangDana.objects.create(user=user, akun_bank=akun_bank, tujuan=tujuan, judul=judul, deskripsi=deskripsi, target=target, gambar=gambar, tanggal_pembuatan=tanggal_pembuatan, tanggal_berakhir=tanggal_berakhir, status_keaktifan=status_keaktifan)
            return redirect('resipien:daftar')
        else:
            formGalang = GalangForm()
            formBank = RekeningBankForm()
    return render(request, "resipien/buat-galang.html", {'formGalang':formGalang, 'formBank':formBank})

def show_daftar_galang(request):     
    data_galang = GalangDana.objects.all()
    context = {
        'data_galang': data_galang,
    }
    return render(request, "resipien/galang-dana.html", context)

def show_detail_galang(request, id):     
    objek_galang = GalangDana.objects.get(id=id)

    context = {
        "galang": objek_galang,
    }
    return render(request, "resipien/detail-galang.html",  context)

def show_add_komentar(request, id):
    if request.method == "POST":
        user = GeneralUser.objects.get(user=request.user)
        objek_galang = GalangDana.objects.get(id=id)
        komentar = request.POST.get('komen')
        tanggal_komentar = datetime.datetime.now()
        Komentar.objects.create(user=user, objek_galang=objek_galang, komentar=komentar, tanggal_komentar=tanggal_komentar)

def show_json(request):
    data_galang = GalangDana.objects.all()
    return HttpResponse(serializers.serialize('json',data_galang), content_type="application/json")

def show_json_komentar(request, id):
    data_komentar = Komentar.objects.filter(objek_galang=id)
    return HttpResponse(serializers.serialize('json',data_komentar), content_type="application/json")


