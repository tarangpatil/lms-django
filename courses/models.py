from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from datetime import date


# Create your models here.
class Course(models.Model):
    name = models.TextField(
        "Course Name",
        max_length=255,
        null=False,
        validators=[MinLengthValidator(5, "Course name must be atleast 5 characters.")],
    )
    description = models.TextField(
        "Course Description",
        null=False,
        validators=[
            MinLengthValidator(20, "Description must be atleast 20 characters.")
        ],
    )
    author = models.ForeignKey(
        "users.InstructorProfile",
        verbose_name="Course Author",
        on_delete=models.CASCADE,
    )
    published_date = models.DateField("Course publish date", null=True, blank=True)

    def __str__(self):
        return self.name

    def is_published(self):
        """Check if the course is published"""
        return self.published_date and self.published_date <= date.today()

    def publish(self):
        if self.published_date is None:
            self.published_date = timezone.now().date()
            self.save()
        return
