from django.db import models

# Create your models here.
class PertanyaanManager(models.Manager):
    def get_by_natural_key(self, kategori, teks_pertanyaan):
        return self.get(kategori=kategori, teks_pertanyaan=teks_pertanyaan)

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

    objects = PertanyaanManager()

    def __str__(self):
        return self.teks_pertanyaan

    # class Meta:
    #     unique_together = [['kategori', 'teks_pertanyaan']]

    def natural_key(self):
        return (self.kategori, self.teks_pertanyaan)

    
class FAQ(models.Model):
    pertanyaan = models.OneToOneField(Pertanyaan, on_delete= models.CASCADE)
    jawaban = models.TextField(max_length=1000)

