from django.contrib import admin
from .models import InstructorProfile, StudentProfile, User

# Register your models here.
admin.site.register(InstructorProfile)
admin.site.register(StudentProfile)
admin.site.register(User)
