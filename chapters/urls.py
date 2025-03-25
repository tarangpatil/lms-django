from django.urls import path
from . import views

# chapter/
urlpatterns = [
    path("<int:pk>/", views.chapter_details, name="chapter_details"),
    path("create/<int:course_pk>", views.create_chapter, name="create_chapter"),
    path(
        "reorder-chapter-down/<int:chapter_pk>",
        views.reorder_chapter_down,
        name="reorder_chapter_down",
    ),
    path(
        "reorder-chapter-up/<int:chapter_pk>",
        views.reorder_chapter_up,
        name="reorder_chapter_up",
    ),
]
