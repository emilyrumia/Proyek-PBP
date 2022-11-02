from distutils.command import upload
from django.utils.timesince import timesince
from django.db import models
from general_user.models import GeneralUser, RekeningBank

class GalangDana(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    akun_bank = models.ForeignKey(RekeningBank, on_delete=models.CASCADE)
    tujuan = models.CharField(max_length=20)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    terkumpul = models.PositiveIntegerField()
    target = models.PositiveIntegerField()
    gambar = models.ImageField(upload_to="resipien/upload", blank=True)
    tanggal_pembuatan = models.DateField(auto_now_add=True)
    tanggal_berakhir = models.DateField(default=None)
    status_keaktifan = models.BooleanField(default=True)

    def get_time_diff(self):
        return timesince(self.tanggal_mulai, self.tanggal_berakhir) 

class KomentarGalang(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    objek_galang = models.ForeignKey(GalangDana, on_delete=models.CASCADE)
    komentar = models.TextField()
    tanggal_komentar = models.DateField(auto_now_add=True)

