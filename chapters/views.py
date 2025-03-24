from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Chapter


# Create your views here.
@login_required
def create_chapter(req, course_pk):
    if req.method != "POST":
        return HttpResponse("method not allowed", status=405)
    course: Course = get_object_or_404(Course, pk=course_pk)

    if req.user.id != course.author.user.id:
        return HttpResponse("Unathorized", status=401)

    new_chapter = Chapter()
    new_chapter.name = req.POST["chapter-name"]
    new_chapter.course = course

    new_chapter.save()

    return redirect("course_details", pk=course_pk)
