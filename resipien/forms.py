from datetime import date
from django import forms
from resipien.models import KomentarGalang
from datetime import date


class GalangForm(forms.Form):

    PRIBADI = "Pribadi"
    KELUARGA = "Keluarga"
    INSTITUSI = "Institusi"
    TEMAN = "Teman"
    LAINNYA = "Lainnya"

    TUJUAN_CHOICES = (
        (PRIBADI, "Pribadi"),
        (KELUARGA, "Keluarga"),
        (INSTITUSI, "Institusi"),
        (TEMAN, "Teman"),
        (LAINNYA, "Lainnya")
    )

    tujuan = forms.ChoiceField(label="Tujuan Keperluan", choices = TUJUAN_CHOICES)
    judul = forms.CharField(label="Judul", max_length=255, widget=forms.TextInput())
    deskripsi = forms.CharField(label="Deskripsi", widget=forms.Textarea(attrs={'rows':15}))
    target = forms.IntegerField(label="Target")
    tanggal_berakhir = forms.DateField(widget = forms.SelectDateWidget(attrs={'style':'width:33%; display: inline-block;'}))
    gambar = forms.ImageField(label="Gambar (Landscape)")

    target.widget.attrs.update({'placeholder':'Rp'})
    deskripsi.widget.attrs.update({'placeholder':'Ceritakan secara lengkap rencana penggunaan dana yang didapat dari galang dana ini'})

    def __init__(self, *args, **kwargs):
        super(GalangForm, self).__init__(*args, **kwargs)
        self.fields['gambar'].required = False

    def clean_tanggal_berakhir(self):
        tanggal_berakhir = self.cleaned_data.get("tanggal_berakhir")
        if (tanggal_berakhir <= date.today()):
            raise forms.ValidationError("End date should be greater than start date.")
        return tanggal_berakhir

class KomentarGalangForm(forms.ModelForm):
    class Meta:
        model = KomentarGalang
        fields = ['komentar']

    komentar = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':3, 'class':'form-control', 'placeholder':'Tambahkan komentar...'}))