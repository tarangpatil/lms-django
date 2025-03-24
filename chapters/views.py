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


@login_required
def reorder_chapter_down(req, chapter_pk):
    if req.method != "POST":
        return HttpResponse("method not allowed", status=405)
    curr_chapter = get_object_or_404(Chapter, pk=chapter_pk)
    next_chapter = get_object_or_404(
        Chapter,
        course=curr_chapter.course,
        chapter_no=curr_chapter.chapter_no + 1,
    )
    next_chapter.chapter_no = 0
    next_chapter.save()
    curr_chapter.chapter_no = curr_chapter.chapter_no + 1
    curr_chapter.save()
    next_chapter.chapter_no = curr_chapter.chapter_no - 1
    next_chapter.save()
    return redirect("course_details", pk=curr_chapter.course.id)


@login_required
def reorder_chapter_up(req, chapter_pk):
    if req.method != "POST":
        return HttpResponse("method not allowed", status=405)

    curr_chapter = get_object_or_404(Chapter, pk=chapter_pk)

    if req.user.id != curr_chapter.course.author.user.id:
        return HttpResponse("Unathorized", status=401)

    prev_chapter = get_object_or_404(
        Chapter,
        course=curr_chapter.course,
        chapter_no=curr_chapter.chapter_no - 1,
    )
    prev_chapter.chapter_no = 0
    prev_chapter.save()
    curr_chapter.chapter_no = curr_chapter.chapter_no - 1
    curr_chapter.save()
    prev_chapter.chapter_no = curr_chapter.chapter_no + 1
    prev_chapter.save()
    return redirect("course_details", pk=curr_chapter.course.id)
