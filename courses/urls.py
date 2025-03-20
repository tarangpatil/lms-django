from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.course_create, name="course_create"),
]
