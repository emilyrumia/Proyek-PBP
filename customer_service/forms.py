from django import forms
from customer_service.models import FAQ, Pertanyaan


class PertanyaanForm(forms.ModelForm):
    # kategori = forms.CharField(max_length=6, choices=Pertanyaan.KATEGORI)
    # teks_pertanyaan = forms.TextInput()

    class Meta:
        model = Pertanyaan
        fields = ["kategori", "teks_pertanyaan"]
        widgets = {
            "kategori": forms.Select(attrs= { "id":"kategori" }),
            "teks_pertanyaan": forms.Textarea(attrs= { "id":"teks_pertanyaan" })
        }


class JawabanForm(forms.ModelForm):
    # jawaban = forms.TextInput()

    class Meta:
        model = FAQ
        # exclude = ["pertanyaan"]
        fields = ["jawaban"]
        widgets = {
            "jawaban": forms.Textarea(attrs= { "id":"jawaban" })
        }



