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
        name='delete_lesson'),
    path('account/details/<lesson_id>', lessons.views.lesson_details, 
        name="lesson_details"),
    path('review/<lesson_id>', lessons.views.create_review,
        name="create_review"),

    path('instructors/', lessons.views.view_instructors,
        name="view_instructors"),
    path('instructor/create', lessons.views.create_instructor,
        name="create_instructor"),
    path('instructor/<instructor_id>/update', lessons.views.update_instructor,
        name="update_instructor"),
    path('instructor/<instructor_id>/delete', lessons.views.delete_instructor,
        name="delete_instructor"),

    path('forum/', lessons.views.view_forum,
        name="view_forum"),
    path('forum/delete/<forum_id>', lessons.views.delete_forum,
        name="delete_forum"),
    path('forum/<forum_id>/comments/', lessons.views.forum_details,
        name="forum_details"),
    path('forum/create/', lessons.views.create_forum,
        name="create_forum"),
    path('forum/<forum_id>/comment', lessons.views.create_comment,
        name="create_comment"),
    path('forum/comment/<comment_id>/delete', lessons.views.delete_comment,
        name="delete_comment"),
    path('forum/comment/<comment_id>/update', lessons.views.update_comment,
        name="update_comment")
]