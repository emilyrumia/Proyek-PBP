from django.urls import path
from lelang import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "lelang"

urlpatterns = [
    path('', views.index, name="show_barang_lelang"),
    path('create_lelang/<int:galang_dana_id>', views.create_lelang, name="create_lelang"),
    path('<int:lelang_id>', views.rincian_lelang, name="rincian_lelang"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)