from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TestimoniList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nama = models.CharField(max_length=50, default="Anonymous", blank=True)
    target = models.CharField(max_length=50, default="-", blank=True)
    pesan = models.TextField()