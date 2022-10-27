from django.urls import path
from customer_service import views

app_name = "customer_service"

urlpatterns = [
    path('', views.show_faq, name="show_faq"),
    path('add-pertanyaan/', views.add_pertanyaan, name="add_pertanyaan"),
    path('add-jawaban/<int:id>/', views.add_jawaban, name="add_jawaban"),
]
