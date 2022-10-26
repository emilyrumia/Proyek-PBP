import datetime
from email.policy import default
from django.utils.timesince import timesince
from distutils.command import upload
from django.db import models
from general_user.models import GeneralUser
from resipien.models import GalangDana

# Create your models here.
class BarangLelang(models.Model):
    ANTIK = "ANTIK"
    PERHIASAN = "PERHIASAN"
    TEKNOLOGI = "TEKNOLOGI"
    FIGURAN = "FIGURAN"
    OTHER = "OTHER"

    KATEGORI_CHOICES = (
        (ANTIK, "Barang Antik"),
        (PERHIASAN, "Perhiasan"),
        (TEKNOLOGI, "Teknologi"),
        (FIGURAN, "Figuran"),
        (OTHER, "Lainnya")
    )
    pelelang = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    galang_dana_tujuan = models.ForeignKey(GalangDana, on_delete=models.RESTRICT)
    nama_barang = models.CharField(max_length=255)
    deskripsi = models.TextField(null=True, blank=True)
    gambar = models.ImageField(default="/lelang/upload/product-image-placeholder.jpg", upload_to="lelang/upload")
    starting_bid = models.PositiveIntegerField()
    bid_tertinggi = models.PositiveIntegerField()
    tanggal_mulai = models.DateTimeField(auto_now_add=True, blank=True)
    tanggal_berakhir = models.DateTimeField()
    status_keaktifan = models.BooleanField(default=True)
    kategori_barang = models.CharField(max_length=100, choices=KATEGORI_CHOICES, default=ANTIK)

    def get_time_diff(self):
        # dummydate = datetime.date(2000,1,1)  # Needed to convert time to a datetime object
        # dt1 = datetime.datetime.combine(dummydate,self.tanggal_mulai)
        # dt2 = datetime.datetime.combine(dummydate,self.tanggal_berakhir)
        return timesince(self.tanggal_mulai, self.tanggal_berakhir)   # Assuming dt2 is the more recent time
    
    def __str__(self) -> str:
        return self.nama_barang

class Bid(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    barang_lelang = models.ForeignKey(BarangLelang, on_delete=models.RESTRICT)
    banyak_bid = models.PositiveIntegerField()

class Komentar(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    barang_lelang = models.ForeignKey(BarangLelang, on_delete=models.CASCADE)
    waktu_ditambahkan = models.DateTimeField(auto_now_add=True, blank=True)
    teks = models.TextField()
