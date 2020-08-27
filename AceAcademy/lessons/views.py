from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
from datetime import date

from .models import *
from .forms import *

from accounts.views import *
from accounts.forms import CreateUserForm
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

# Open to Public

def home(request):
    return render(request, 'lessons/home.html')

def view_lessons_public(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/view_lessons_public.html', {
        'lessons': lessons
    })

def view_instructors_public(request):
    instructors = Instructor.objects.all()
    return render(request, 'lessons/view_instructors_public.html', {
        'instructors': instructors
    })


# REGARDING LESSONS
@login_required(login_url='login')
def view_lessons(request):
    lessons = Lesson.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        lessons = lessons.filter(queries)
    search_lesson = SearchForm(request.GET)
    return render(request, 'lessons/view_lessons.html', {
        'lessons': lessons,
        'search_lesson': search_lesson
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_lesson(request):
    if request.method == 'POST':
        create_lesson = LessonForm(request.POST)
        print(request.POST)
        if create_lesson.is_valid():
            create_lesson.save()
            messages.success(request, f"New lesson has been created!")
            return redirect(reverse('view_all_lessons'))
        else:
            return render(request, 'lessons/create_lesson.html', {
                'form': create_lesson
            })
    else:
        create_lesson = LessonForm()
        return render(request, 'lessons/create_lesson.html', {
            'form': create_lesson
        })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_lesson(request, lesson_id):
    lesson_being_updated = get_object_or_404(Lesson, pk=lesson_id)

    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, instance=lesson_being_updated)

        if lesson_form.is_valid():
            lesson_form.save()
            return redirect(reverse('view_all_lessons'))

        else:
            return render(request, 'lessons/update_lesson.html', {
                'form': lesson_form
            })

    else:
        lesson_form = LessonForm(instance=lesson_being_updated)
        return render(request, 'lessons/update_lesson.html', {
            'form': lesson_form
        })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_lesson(request, lesson_id):
    lesson_to_delete = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        lesson_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'lessons/delete_lesson.html', {
            'lesson': lesson_to_delete
        })

def lesson_details(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/lesson_details.html', {
        'lesson':lesson
    })

def create_review(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == "POST":
        form = AddReview(request.POST)
        review = form.save(commit=False)
        review.lesson_reviewed = lesson
        review.review_date = date.today()
        review.reviewer = request.user
        review.save()
        return redirect(reverse('view_all_lessons'))
    else:
        form = AddReview()
        return render(request, 'lessons/create_review.html', {
            'form': form
        })

def create_comment(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review_commented = review
            comment.commentor=request.user
            comment.comment_date = date.today()
            comment.save()
            return redirect(reverse('view_all_lessons'))
    else:
        form = CommentForm()
        return render(request, 'lessons/create_comment.html', {
                'form': form,
                'review': review
            })
