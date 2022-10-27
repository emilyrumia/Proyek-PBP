from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customer_service.forms import JawabanForm, PertanyaanForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core import serializers 



from customer_service.models import FAQ, Pertanyaan

# Create your views here.
def index(request):
    return HttpResponse("Ini halaman customer service")

def show_faq(request):
    # list_faq = FAQ.objects.filter(is_answered=True)

    form_jawaban = JawabanForm(request.POST)
    form_pertanyaan = PertanyaanForm(request.POST)
    list_faq = FAQ.objects.all()
    list_pertanyaan = Pertanyaan.objects.filter(is_answered=False)

    context = { 
        "form_jawaban" : form_jawaban,
        'form_pertanyaan': form_pertanyaan,
        "list_faq" : list_faq,
        "list_pertanyaan" : list_pertanyaan

    }

    return render(request, "faq.html", context)


@login_required(login_url='/general_user/login/')
def add_jawaban(request, id):
    # form_jawaban = JawabanForm()

    # if request.method == 'POST':
    form_jawaban = JawabanForm(request.POST)
        # form_jawaban.instance.user = request.user
    if form_jawaban.is_valid():
        faq = form_jawaban.save(commit=False)
        pertanyaan = Pertanyaan.objects.get(id=id)
        pertanyaan.is_answered = True
        pertanyaan.save()
        faq.pertanyaan = pertanyaan
        faq.save()
        return redirect('customer_service:show_faq')

def getJSON(request):
    faqs = FAQ.objects.all()
    return HttpResponse(serializers.serialize('json', faqs), content_type='application/json')

# @login_required(login_url='/general_user/login/')
# def add_pertanyaan(request):
#     kategori = request.POST.get('kategori')
#     teks_pertanyaan = request.POST.get('teks_pertanyaan')
#     new_pertanyaan = Pertanyaan(kategori=kategori, teks_pertanyaan=teks_pertanyaan)
#     new_pertanyaan.save()
#     return redirect('customer_service:show_faq')

@login_required(login_url='/general_user/login/')
def add_pertanyaan(request):
    form_pertanyaan = PertanyaanForm()

    if request.method == 'POST':
        form_pertanyaan = PertanyaanForm(request.POST)
        if form_pertanyaan.is_valid():
            form_pertanyaan.save()
            return redirect('customer_service:show_faq')