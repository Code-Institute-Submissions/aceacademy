from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Lesson
from .forms import LessonForm, SearchForm
from django.db.models import Q
from accounts.views import registerPage, loginPage, logoutUser

# Create your views here.
@login_required(login_url='login')
def view_lessons(request):
    lessons = Lesson.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        lessons = lessons.filter(queries)
    search_lesson = SearchForm(request.GET
    )
    return render(request, 'lessons/view_lessons.html', {
        'lessons': lessons,
        'search_lesson': search_lesson
    })

def create_lesson(request):
    if request.method == 'POST':
        create_lesson = LessonForm(request.POST)
        print(request.POST)
        if create_lesson.is_valid():
            create_lesson.save()
            messages.success(request, f"New lesson has been created!")
            return redirect(reverse(index))
        else:
            return render(request, 'lessons/create_lesson.html', {
                'form': create_lesson
            })
    else:
        create_lesson = LessonForm()
        return render(request, 'lessons/create_lesson.html', {
            'form': create_lesson
        })

def update_lesson(request, lesson_id):
    lesson_being_updated = get_object_or_404(Lesson, pk=lesson_id)

    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, instance=lesson_being_updated)

        if lesson_form.is_valid():
            lesson_form.save()
            return redirect(reverse(index))

        else:
            return render(request, 'lessons/update_lesson.html', {
                'form': lesson_form
            })

    else:
        lesson_form = LessonForm(instance=lesson_being_updated)
        return render(request, 'lessons/update_lesson.html', {
            'form': lesson_form
        })

def delete_lesson(request, lesson_id):
    lesson_to_delete = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        lesson_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'lessons/delete_lesson.html', {
            'lesson': lesson_to_delete
        })
