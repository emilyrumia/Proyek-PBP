
import email
from general_user.models import GeneralUser, RekeningBank
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    error_messages = {
        'no_ponsel_mismatch': ("Nomor ponsel tidak valid."),
    }
    no_ponsel = forms.CharField(max_length=16, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # specify the name of model to use
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password", "no_ponsel"]

    def clean_no_ponsel(self):
        no_ponsel = self.cleaned_data.get("no_ponsel")
        if len(no_ponsel) > 16 or not no_ponsel.isnumeric():
            raise forms.ValidationError(
                self.error_messages['no_ponsel_mismatch'],
                code='no_ponsel_mismatch',
            )
        return no_ponsel

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class RekeningBankForm(forms.ModelForm):
    error_messages = {
        'rekening_mismatch': ("Nomor rekening tidak valid."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_bank'].widget.attrs.update({'class': 'select form-select'})
        
    class Meta:
        model = RekeningBank
        fields = ['nama_bank', 'no_rekening', 'nama_pemilik']

    def clean_no_rekening(self):
        no_rekening = self.cleaned_data.get("no_rekening")
        if len(no_rekening) > 16 or not no_rekening.isnumeric():
            raise forms.ValidationError(
                self.error_messages['rekening_mismatch'],
                code='rekening_mismatch',
            )
        return no_rekening