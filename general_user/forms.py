from operator import imod
from django import forms
from general_user.models import *
from django.contrib.auth.forms import UserCreationForm  

class GeneralUserRegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        'no_rekening_mismatch': ("Nomor rekening tidak valid."),
        'nik_mismatch': ("NIK tidak valid.")
    }
    first_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))
    # specify the name of model to use
    class Meta:
        model = GeneralUser
        fields = ["first_name", "last_name", "email", "nik", "no_rekening", "username"]
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_no_rekening(self):
        no_rekening = self.cleaned_data.get("no_rekening")
        if len(no_rekening) > 16 or not no_rekening.isnumeric():
            raise forms.ValidationError(
                self.error_messages['no_rekening_mismatch'],
                code='no_rekening_mismatch',
            )
        return no_rekening

    def clean_nik(self):
        nik = self.cleaned_data.get("nik")
        if len(nik) != 16 or not nik.isnumeric():
            raise forms.ValidationError(
                self.error_messages['nik_mismatch'],
                code='nik_mismatch',
            )
        return nik