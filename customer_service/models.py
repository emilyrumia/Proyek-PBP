from tkinter import CASCADE
from django.db import models

# Create your models here.
class Pertanyaan(models.Model):
    teks_pertanyaan = models.TextField();

    
class FAQ(models.Model):
    pertanyaan = models.OneToOneField(Pertanyaan, on_delete=CASCADE)
    jawaban = models.TextField()

