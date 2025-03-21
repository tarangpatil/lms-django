import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from users.models import InstructorProfile
from .models import Course


# Create your views here.
def course_create(req):
    if not req.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    user_ins = InstructorProfile.objects.filter(user__id=req.user.id)
    if user_ins.count() < 1:
        return HttpResponse("Only instructors can create courses", status=401)

    if req.method == "POST":
        course_name = req.POST["course-name"]
        course_desc: str = req.POST["course-description"]
        if not course_name:
            return HttpResponse("Course name is required", status=400)
        if not course_desc:
            return HttpResponse("Course description is required", status=400)
        new_course = Course()
        new_course.name = course_name
        new_course.description = course_desc.replace("\n", "")
        new_course.author = user_ins[0]
        new_course.save()
        return redirect("home_page")
    return render(req, "courses/course_create.html")


@login_required
def course_edit(req, pk):
    user_ins = InstructorProfile.objects.filter(user__id=req.user.id)

    if user_ins.count() < 1:
        return HttpResponse("Only instructors can edit courses", status=401)

    course = get_object_or_404(Course, pk=pk)

    if course.author.user.id != req.user.id:
        return HttpResponse("Unauthorized", status=401)

    if req.method == "PUT":
        try:
            PUT_BODY = json.loads(req.body)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)
        
        course_name = PUT_BODY["course_name"]
        course_description = PUT_BODY["course_description"]
        to_publish = PUT_BODY["toPublish"]
        course.name = course_name
        course.description = course_description
        course.save()
        
        if to_publish:
            course.publish()
        return redirect("home_page")
    return render(req, "courses/course_edit.html", {"course": course})
