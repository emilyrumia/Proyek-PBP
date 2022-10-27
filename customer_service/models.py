from email.policy import default
from random import choices
from django.db import models
from general_user.models import GeneralUser

# Create your models here.
class Pertanyaan(models.Model):

    UMUM = "UMUM"
    LELANG = "LELANG"
    GALANG = "GALANG"

    KATEGORI = (
        ("UMUM", "Umum"),
        ("LELANG", "Lelang"),
        ("GALANG", "Galang Dana")
    )

    # user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    kategori = models.CharField(max_length=6, choices=KATEGORI, default=UMUM);
    teks_pertanyaan = models.TextField(max_length=1000)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.teks_pertanyaan

    
class FAQ(models.Model):
    pertanyaan = models.OneToOneField(Pertanyaan, on_delete= models.CASCADE)
    jawaban = models.TextField(max_length=1000)

