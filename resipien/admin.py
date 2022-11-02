from telnetlib import GA
from django.contrib import admin

from resipien.models import GalangDana, KomentarGalang

# Register your models here.
admin.site.register(GalangDana)
admin.site.register(KomentarGalang)