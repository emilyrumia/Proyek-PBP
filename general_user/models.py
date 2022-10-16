from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneralUser(User):
    nik = models.CharField(max_length=16, unique=True, verbose_name="NIK")
    no_rekening = models.CharField(max_length=16, unique=True, verbose_name="Nomor Rekening")
