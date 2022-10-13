from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
