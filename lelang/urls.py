from django.urls import path
from lelang import views

app_name = "lelang"

urlpatterns = [
    path('', views.index, name="show_barang_lelang"),
]
