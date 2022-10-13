from django.urls import path
from resipien import views

app_name = "resipien"

urlpatterns = [
    path('', views.homepage, name="homepage"),
]