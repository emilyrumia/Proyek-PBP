from django.urls import path
from testimoni import views

app_name = "testimoni"

urlpatterns = [
    path('', views.show_testimoni, name="tampilan_testimoni"),
    path('add-testimoni/', views.add_testimoni, name='add_testimoni')
]