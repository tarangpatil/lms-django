from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.course_create, name="course_create"),
    path("edit/<int:pk>/", views.course_edit, name="course_edit"),
]
