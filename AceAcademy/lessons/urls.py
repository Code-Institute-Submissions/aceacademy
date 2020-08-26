from django.contrib import admin
from django.urls import path, include
import lessons.views

urlpatterns = [
    path('', lessons.views.view_lessons, 
        name='view_all_lessons'),
    path('create', lessons.views.create_lesson,
        name='create_lesson'),
    path('update/<lesson_id>', lessons.views.update_lesson,
        name='update_lesson'),
    path('delete/<lesson_id>', lessons.views.delete_lesson,
        name='delete_lesson')
]