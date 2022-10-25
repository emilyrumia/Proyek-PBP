from email.policy import default
from django.db import models
from general_user.models import GeneralUser, RekeningBank

class GalangDana(models.Model):
    PRIBADI = "PRIBADI"
    KERABAT = "KERABAT"
    LEMBAGA = "LEMBAGA"
    OTHER = "OTHER"

    KEPERLUAN_CHOICES = (
        (PRIBADI, "Pribadi"),
        (KERABAT, "Kerabat/Keluarga"),
        (LEMBAGA, "Institusi/Lembaga"),
        (OTHER, "Lainnya")
    )
    penggalang = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    rekening_bank = models.ForeignKey(RekeningBank, on_delete=models.RESTRICT)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField(null=True, blank=True)
    gambar = models.ImageField()
    target_galang_dana = models.PositiveIntegerField()
    tanggal_berakhir = models.DateField()
    status_keaktifan = models.BooleanField(default=True)
    tujuan_keperluan = models.CharField(max_length=100, choices=KEPERLUAN_CHOICES, default=PRIBADI)

    def __str__(self) -> str:
        return self.judul