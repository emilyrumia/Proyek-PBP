from django.db import models

# Create your models here.
class TestimoniList(models.Model):
    nama = models.CharField(max_length=50, default="Anonymous")
    title = models.CharField(max_length=50)
    target = models.CharField(max_length=50, default="-")
    pesan = models.TextField()