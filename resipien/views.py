# from lib2to3.pgen2.token import GREATER
from inspect import stack
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from general_user.forms import RekeningBankForm
from general_user.models import GeneralUser, RekeningBank
from resipien.models import GalangDana, Komentar
from resipien.forms import GalangForm, KomentarForm
from django.contrib import messages
import datetime
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def homepage(request):
    if not request.user.is_authenticated:
        return redirect('general_user:homepage')
    else:
        return render(request, "galang-dana.html")

@login_required(login_url='/general_user/login/')
@csrf_protect
def show_buat_galang(request):
    formGalang = GalangForm()
    if request.method == 'POST':
        formGalang = GalangForm(request.POST, request.FILES)
        if formGalang.is_valid():
            user = GeneralUser.objects.get(user=request.user)
            tujuan = formGalang.cleaned_data["tujuan"]
            judul = formGalang.cleaned_data["judul"]
            deskripsi = formGalang.cleaned_data["deskripsi"]
            target = formGalang.cleaned_data["target"]
            gambar = formGalang.cleaned_data["gambar"]
            tanggal_pembuatan = datetime.datetime.now()
            tanggal_berakhir = datetime.datetime.now()
            status_keaktifan = True
            GalangDana.objects.create(user=user, tujuan=tujuan, judul=judul, deskripsi=deskripsi, target=target, gambar=gambar, tanggal_pembuatan=tanggal_pembuatan, tanggal_berakhir=tanggal_berakhir, status_keaktifan=status_keaktifan)
            return redirect('resipien:daftar')
        else:
            formGalang = GalangForm()
    return render(request, "resipien/buat-galang.html", {'formGalang':formGalang})

def show_daftar_galang(request):     
    data_galang = GalangDana.objects.all()
    context = {
        'data_galang': data_galang,
    }
    return render(request, "resipien/galang-dana.html", context)

def show_detail_galang(request, id):     
    formKomentar = KomentarForm()
    objek_galang = GalangDana.objects.get(id=id)
    data_komentar = Komentar.objects.filter(objek_galang=objek_galang)

    context = {
        "formKomentar": formKomentar,
        "galang": objek_galang,
        "data_komentar": data_komentar,
    }
    return render(request, "resipien/detail-galang.html",  context)



def show_json(request):
    data_galang = GalangDana.objects.all()
    return HttpResponse(serializers.serialize('json',data_galang), content_type="application/json")


