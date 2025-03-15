from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model that extends AbstractUser."""

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.email}"


class InstructorProfile(models.Model):
    """Profile for instructors."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="instructor_profile"
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class StudentProfile(models.Model):
    """Profile for students."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
