from django.urls import path
from testimoni import views

app_name = "testimoni"

urlpatterns = [
    path('', views.show_testimoni, name="show_testimoni"),
    path('json/', views.show_testimoni_json, name="show_testimoni_json"),
    path('add-testimoni/', views.add_testimoni, name="add_testimoni")
]