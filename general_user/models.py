
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

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

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=64, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

class GeneralUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_resipien = models.BooleanField(default=False)
    akun_bank = models.OneToOneField(RekeningBank, on_delete=models.RESTRICT)
    no_ponsel = models.CharField(max_length=16, unique=True)

# @receiver(post_save, sender=CustomUser)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         GeneralUser.objects.create(user=instance)
#     instance.person.save()