from django.shortcuts import render, redirect
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
        course_desc = req.POST["course-description"]
        if not course_name:
            return HttpResponse("Course name is required", status=400)
        if not course_desc:
            return HttpResponse("Course description is required", status=400)
        new_course = Course()
        new_course.name = course_name
        new_course.description = course_desc
        new_course.author = user_ins[0]
        new_course.save()
        return redirect("home_page")
    return render(req, "courses/course_create.html")
