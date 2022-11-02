from django import forms
from customer_service.models import FAQ, Pertanyaan


class PertanyaanForm(forms.ModelForm):
    class Meta:
        model = Pertanyaan
        fields = ["kategori", "teks_pertanyaan"]
        widgets = {
            "kategori": forms.Select(attrs= { "id":"kategori" }),
            "teks_pertanyaan": forms.Textarea(attrs= { "id":"teks_pertanyaan" })
        }


class JawabanForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ["jawaban"]
        widgets = {
            "jawaban": forms.Textarea(attrs= { "id":"jawaban" })
        }



