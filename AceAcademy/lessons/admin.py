from django.contrib import admin
from .models import Lesson, Instructor, Reviews

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Reviews)