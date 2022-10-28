from django import forms

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
    judul = forms.CharField(label="Judul", max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    deskripsi = forms.CharField(label="Deskripsi", widget=forms.Textarea(attrs={'rows':15, 'class':'form-control'}))
    target = forms.CharField(label="Target", widget=forms.TextInput(attrs={'class':'form-control', 'id': 'input-target'}))
    gambar = forms.ImageField(label="Gambar")

    tujuan.widget.attrs.update({'class': 'form-control'})
    deskripsi.widget.attrs.update({'class': 'form-control'})
    gambar.widget.attrs.update({'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super(GalangForm, self).__init__(*args, **kwargs)
        self.fields['gambar'].required = False
