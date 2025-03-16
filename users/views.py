from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import User, InstructorProfile


def home_page(req):
    context = {"user": None}
    if req.user.is_authenticated:
        context["user"] = req.user
    return render(req, "users/home_page.html", context=context)


def logout_user(req):
    logout(req)
    return redirect("login")


def login_user(req):
    if req.method == "POST":
        email = req.POST["email"]
        password = req.POST["password"]
        user = authenticate(req, email=email, password=password)
        if user is not None:
            login(req, user)
            return redirect("home_page")
        else:
            return redirect("login")
    else:
        print("AUTH", req.user)
        return render(req, "users/login.html")


def register_instructor(req):
    if req.method == "POST":
        new_user = User.objects.create(
            first_name=req.POST["first-name"],
            last_name=req.POST["last-name"],
            email=req.POST["email"],
        )
        new_user.set_password(req.POST["password"])
        new_user.save()
        new_instructor = InstructorProfile()
        new_instructor.user = new_user
        new_instructor.bio = ""
        new_instructor.save()
        login(req, new_user)
        return redirect("home_page")
    return render(req, "users/register_instructor.html", {})
