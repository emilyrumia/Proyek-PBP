from django.db import models
from general_user.models import GeneralUser, RekeningBank

class GalangDana(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    akun_bank = models.ForeignKey(RekeningBank, on_delete=models.CASCADE)
    tujuan = models.CharField(max_length=20)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    target = models.CharField(max_length=30)
    gambar = models.ImageField(upload_to="resipien/", blank=True)
    tanggal_pembuatan = models.DateField(auto_now_add=True)
    tanggal_berakhir = models.DateField(default=None)
    status_keaktifan = models.BooleanField(default=True)

class KomentarGalangDana(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    objek_galang = models.ForeignKey(GalangDana, on_delete=models.CASCADE)
    komentar = models.TextField()
    tanggal_komentar = models.DateField(auto_now_add=True)
