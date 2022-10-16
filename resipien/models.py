from django.db import models

# Create your models here.
class ResipienDonasi(models.Model):
    no_rekening = models.CharField(max_length=16, unique=True)