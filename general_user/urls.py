from django.urls import path
from general_user import views

app_name = "general_user"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
    # path('galang/<id>', views.get_galang, name="get_galang"),
    # path('lelang/<id>', views.get_lelang, name="get_lelang"),
    # path('galang/json/', views.show_json_galang, name="show_json_galang"),
    # path('lelang/json/', views.show_json_lelang, name="show_json_lelang"),

]
