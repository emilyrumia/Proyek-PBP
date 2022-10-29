from django.db import models
from general_user.models import GeneralUser
from django.contrib.auth.models import User

# Create your models here.
class TestimoniList(models.Model):
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pesan = models.TextField()