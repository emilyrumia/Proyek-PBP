from ast import arg
from cmath import log
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from general_user.models import GeneralUser
from lelang.forms import BarangLelangForm, BiddingForm, KomentarForm
from lelang.models import BarangLelang, Bid, Komentar
from resipien.models import GalangDana
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    barang_lelang = BarangLelang.objects.all()

    context = {
        "items": barang_lelang
    }
    
    return render(request, "lelang/show_barang_lelang.html", context)

@login_required(login_url='/login')
def create_lelang(request, galang_dana_id):
    form = BarangLelangForm()
    if (request.method == "POST"):
        form = BarangLelangForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST.get("starting_bid"))
            item = form.save(commit=False)
            item.galang_dana_tujuan = GalangDana.objects.get(pk=int(galang_dana_id))
            item.pelelang = GeneralUser.objects.get(user=request.user)
            item.bid_tertinggi = item.starting_bid
            item.save()

            return HttpResponseRedirect(reverse("lelang:rincian_lelang", args=[item.pk]))
    
    context = {
        "form": form
    }
    return render(request, "lelang/create_lelang.html", context)

def rincian_lelang(request, lelang_id):
    form = BiddingForm()
    form_komentar = KomentarForm()
    barang_lelang = BarangLelang.objects.get(pk=int(lelang_id))
    bids = Bid.objects.filter(barang_lelang=lelang_id).order_by('-banyak_bid')
    bid_tertinggi = bids.first()
    semua_komentar = Komentar.objects.filter(barang_lelang=lelang_id)

    context = {
        "form": form,
        "form_komentar": form_komentar,
        "item": barang_lelang,
        "bids": bids,
        "bid_tertinggi": bid_tertinggi,
        "semua_komentar": semua_komentar
    }
    return render(request, "lelang/rincian_lelang.html", context)

def bid_barang_lelang(request, lelang_id):
    if request.method == "POST":
        form = BiddingForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            barang_lelang = BarangLelang.objects.get(pk=lelang_id)
            bid.user = GeneralUser.objects.get(user=request.user)
            bid.barang_lelang = barang_lelang
            if bid.banyak_bid >= barang_lelang.bid_tertinggi:
                barang_lelang.bid_tertinggi = bid.banyak_bid
                barang_lelang.save()
                bid.save()
        return HttpResponseRedirect(reverse("lelang:rincian_lelang", args=[lelang_id]))

def komentar_barang_lelang(request, lelang_id):
    form = KomentarForm(request.POST)
    if form.is_valid():
        komentar = form.save(commit=False)
        komentar.user = GeneralUser.objects.get(user=request.user)
        komentar.barang_lelang = BarangLelang.objects.get(pk=lelang_id)
        komentar.save()
    return HttpResponseRedirect(reverse("lelang:rincian_lelang", args=[lelang_id]))
