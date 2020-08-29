from django.contrib import admin
from .models import Lesson, Instructor, Reviews, Forum, Comment

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Reviews)
admin.site.register(Forum)
admin.site.register(Comment)