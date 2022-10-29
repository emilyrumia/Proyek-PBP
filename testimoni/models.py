from django.db import models
from general_user.models import GeneralUser

# Create your models here.
class TestimoniList(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50, default="Anonymous")
    title = models.CharField(max_length=50)
    target = models.CharField(max_length=50, default="-")
    pesan = models.TextField()