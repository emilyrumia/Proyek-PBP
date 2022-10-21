
from operator import imod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.contrib.auth.models import User

class RekeningBank(models.Model):
    MANDIRI = "MANDIRI"
    BNI = "BNI"
    BCA = "BCA"
    BRI = "BRI"
    OTHER = "OTHER"

    BANK_CHOICES = (
        (MANDIRI, "Mandiri"),
        (BNI, "BNI"),
        (BCA, "BCA"),
        (BRI, "BRI"),
        (OTHER, "Lainnya")
    )

    nama_pemilik = models.CharField(max_length=255)
    nama_bank = models.CharField(max_length=8, choices=BANK_CHOICES, default=MANDIRI)
    no_rekening = models.CharField(max_length=16, unique=True)


class GeneralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_resipien = models.BooleanField(default=False)
    akun_bank = models.OneToOneField(RekeningBank, on_delete=models.RESTRICT)
    no_ponsel = models.CharField(max_length=16, unique=True)

