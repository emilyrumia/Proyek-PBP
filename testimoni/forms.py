from django import forms
from testimoni.models import TestimoniList

class TestimoniForm(forms.ModelForm) :
    class Meta:
        model = TestimoniList
        fields = ['nama', 'target', 'pesan']