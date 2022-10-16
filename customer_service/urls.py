from django.urls import path
from customer_service import views

app_name = "customer_service"

urlpatterns = [
    path('', views.index, name="tanya_cs"),
]
