from django.urls import path
from testimoni import views

app_name = "testimoni"

urlpatterns = [
    path('', views.index, name="tampilan_testimoni"),
]