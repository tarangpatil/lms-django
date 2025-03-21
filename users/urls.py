from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("instructor/register/", views.register_instructor, name="register_instructor"),
]
