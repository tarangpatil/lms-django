from django.urls import path
from . import views

# chapter/
urlpatterns = [
    path("create/<int:course_pk>", views.create_chapter, name="create_chapter"),
]
