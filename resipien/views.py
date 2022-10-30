# from lib2to3.pgen2.token import GREATER
from inspect import stack
import json
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from general_user.forms import RekeningBankForm
from general_user.models import GeneralUser, RekeningBank
from lelang.views import bid_barang_lelang
from resipien.models import GalangDana, KomentarGalangDana
from resipien.forms import GalangForm
from lelang.models import BarangLelang, Bid
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
    target_donasi = objek_galang.target
    target_donasi = int(target_donasi.replace(".", "")[3:])

    barang_lelang_penyumbang = BarangLelang.objects.filter(galang_dana_tujuan=objek_galang)
    bid_barang_lelang_selesai = set()
    jumlah_semua_bid = 0
    for barang_lelang in barang_lelang_penyumbang:
        curr_highest_bid = Bid.objects.filter(barang_lelang=barang_lelang).order_by('-banyak_bid').first()
        bid_barang_lelang_selesai.add(curr_highest_bid)
        if curr_highest_bid is not None:
            jumlah_semua_bid += 0.7 * curr_highest_bid.banyak_bid
        
    rasio_donasi = jumlah_semua_bid/target_donasi * 100
    context = {
        "galang": objek_galang,
        "rasio_donasi": rasio_donasi,
        "barang_lelang_penyumbang": barang_lelang_penyumbang,
        "bids_tertinggi": bid_barang_lelang_selesai,
        "jumlah_semua_bid": jumlah_semua_bid
    }
    return render(request, "resipien/detail-galang.html",  context)

def show_add_komentar(request, id):
    if request.method == "POST":
        user = GeneralUser.objects.get(user=request.user)
        objek_galang = GalangDana.objects.get(id=id)
        komentar = request.POST.get('komen')
        tanggal_komentar = datetime.datetime.now()
        KomentarGalangDana.objects.create(user=user, objek_galang=objek_galang, komentar=komentar, tanggal_komentar=tanggal_komentar)

def show_json(request):
    data_galang = GalangDana.objects.all()
    return HttpResponse(serializers.serialize('json',data_galang), content_type="application/json")

def show_json_komentar(request, id):
    data_komentar = KomentarGalangDana.objects.filter(objek_galang=id)
    return HttpResponse(serializers.serialize('json',data_komentar), content_type="application/json")


