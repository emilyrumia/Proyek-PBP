from cmath import log
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from general_user.models import GeneralUser
from lelang.forms import BarangLelangForm, BiddingForm
from lelang.models import BarangLelang
from resipien.models import GalangDana
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    barang_lelang = BarangLelang.objects.all()
    context = {"items": barang_lelang}
    
    return render(request, "lelang/show_barang_lelang.html", context)

@login_required(login_url='/login')
def create_lelang(request, galang_dana_id):
    form = BarangLelangForm()
    if (request.method == "POST"):
        form = BarangLelangForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.galang_dana_tujuan = GalangDana.objects.get(pk=int(galang_dana_id))
            item.pelelang = GeneralUser.objects.get(user=request.user)
            item.save()

            return HttpResponseRedirect(reverse("lelang:rincian_lelang", args=[item.pk]))
    
    context = {
        "form": form
    }
    return render(request, "lelang/create_lelang.html", context)

def rincian_lelang(request, lelang_id):
    form = BiddingForm()
    barang_lelang = BarangLelang.objects.get(pk=int(lelang_id))
    if (request.method == "POST"):
        form = BiddingForm(request.POST)
        pass

    context = {
        "form": form,
        "item": barang_lelang
    }
    return render(request, "lelang/rincian_lelang.html", context)