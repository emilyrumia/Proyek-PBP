from django.db import models

# Create your models here.
class TestimoniList(models.Model):
    nama = models.CharField(max_length=50, default="Anonymous", blank=True)
    title = models.CharField(max_length=50)
    target = models.CharField(max_length=50, default="-", blank=True)
    pesan = models.TextField()