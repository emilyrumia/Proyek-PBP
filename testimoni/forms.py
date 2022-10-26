from django import forms
from django import forms
from testimoni.models import testimoniList

class TestimoniForm(forms.ModelForm) :
    class Meta:
        model = testimoniList
        fields = ['nama','pesan']