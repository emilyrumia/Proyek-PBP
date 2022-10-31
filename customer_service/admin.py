from django.contrib import admin
from customer_service.models import FAQ, Pertanyaan

# Register your models here.
admin.site.register(Pertanyaan)
admin.site.register(FAQ)