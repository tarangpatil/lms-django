from django.db import models
from django.core.validators import MinLengthValidator
from courses.models import Course


# Create your models here.
class Chapter(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "chapter_no"], name="unique_course_chapter_no"
            )
        ]

    name = models.CharField(
        "Chapter name",
        max_length=255,
        validators=[
            MinLengthValidator(5, "Chapter name cannot be less than 5 characters")
        ],
        null=False,
    )
    chapter_no = models.IntegerField(null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)

    def save(self, *args, **kwargs):
        if not self.chapter_no:
            last_chapter = (
                Chapter.objects.filter(course=self.course)
                .order_by("-chapter_no")
                .first()
            )
            if last_chapter:
                self.chapter_no = last_chapter.chapter_no + 1
            else:
                self.chapter_no = 1

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
