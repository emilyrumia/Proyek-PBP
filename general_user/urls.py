from django.urls import path
from general_user import views

app_name = "general_user"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
]
