from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TestimoniList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pesan = models.TextField()