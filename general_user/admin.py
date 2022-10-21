from django.contrib import admin
from general_user.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AuthenticationForm

# Register your models here.

admin.site.register(RekeningBank)
admin.site.register(CustomUser)
admin.site.register(GeneralUser)