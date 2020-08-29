from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.db.models import Q
from datetime import date

from .models import Instructor, Reviews, Lesson, Forum, Comment
from .forms import InstructorProfile, LessonForm, AddReview, AddForum, SearchForm, SearchInstructor, AddComment

# Open to Public

def home(request):
    return render(request, 'lessons/home.html')


# About lessons

def view_lessons_public(request):
    search_lesson = SearchForm(request.GET)
    lessons = Lesson.objects.all()

    if request.GET:
        query = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query & Q(title__icontains=title)

        lessons = lessons.filter(query)
        return render(request, 'lessons/view_lessons_public.html', {
            'lessons': lessons,
            'search_lesson': search_lesson
        })
    else:
        lessons = Lesson.objects.all()
        return render(request, 'lessons/view_lessons_public.html', {
            'search_lesson': search_lesson,
            'lessons': lessons
        })


@login_required()
def view_lessons(request):
    search_lesson = SearchForm(request.GET)
    lessons = Lesson.objects.all()

    if request.GET:
        query = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query & Q(title__icontains=title)

        lessons = lessons.filter(query)
        return render(request, 'lessons/view_lessons.html', {
            'lessons': lessons,
            'search_lesson': search_lesson
        })
    else:
        lessons = Lesson.objects.all()
        return render(request, 'lessons/view_lessons.html', {
            'search_lesson': search_lesson,
            'lessons': lessons
        })


@permission_required('lessons.create_lesson', raise_exception=True)
@login_required()
def create_lesson(request):
    if request.method == 'POST':
        create_lesson = LessonForm(request.POST)
        if create_lesson.is_valid():
            create_lesson.save()
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

@permission_required('lessons.update_lesson', raise_exception=True)
@login_required()
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

@permission_required('lessons.delete_lesson', raise_exception=True)
@login_required()
def delete_lesson(request, lesson_id):
    lesson_to_delete = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        lesson_to_delete.delete()
        return redirect('view_all_lessons')
    else:
        return render(request, 'lessons/delete_lesson.html', {
            'lesson': lesson_to_delete
        })

@login_required()
def lesson_details(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/lesson_details.html', {
        'lesson':lesson
    })

@login_required()
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
            'form': form,
            'lesson': lesson
        })

        


# About Instructors

def view_instructors_public(request):
    instructors = Instructor.objects.all()
    search_instructor = SearchInstructor(request.GET)

    if request.GET:
        query = ~Q(pk__in=[])

        if 'instructor_full_name' in request.GET and request.GET['instructor_full_name']:
            instructor_full_name = request.GET['instructor_full_name']
            query = query & Q(instructor_full_name__icontains=instructor_full_name)

        instructors = instructors.filter(query)
        return render(request, 'lessons/view_instructors_public.html', {
            'search_instructor': search_instructor,
            'instructors': instructors
        })
        
    else:
        instructors = Instructor.objects.all()
    return render(request, 'lessons/view_instructors_public.html', {
        'search_instructor': search_instructor,
        'instructors': instructors
    })

@login_required()
def view_instructors(request):
    instructors = Instructor.objects.all()
    search_instructor = SearchInstructor(request.GET)

    if request.GET:
        query = ~Q(pk__in=[])

        if 'instructor_full_name' in request.GET and request.GET['instructor_full_name']:
            instructor_full_name = request.GET['instructor_full_name']
            query = query & Q(instructor_full_name__icontains=instructor_full_name)

        instructors = instructors.filter(query)
        return render(request, 'lessons/view_instructors.html', {
            'search_instructor': search_instructor,
            'instructors': instructors
        })
        
    else:
        instructors = Instructor.objects.all()
    return render(request, 'lessons/view_instructors.html', {
        'search_instructor': search_instructor,
        'instructors': instructors
    })


@permission_required('lessons.create_instructor', raise_exception=True)
@login_required()
def create_instructor(request):
    if request.method == 'POST':
        create_instructor = InstructorProfile(request.POST)
        if create_instructor.is_valid():
            create_instructor.save()
            return redirect(reverse('view_instructors'))
        else:
            return render(request, 'lessons/create_instructor.html', {
                'form': create_instructor
            })
    else:
        create_instructor = InstructorProfile()
        return render(request, 'lessons/create_instructor.html', {
            'form': create_instructor
        })

@permission_required('lessons.update_instructor', raise_exception=True)
@login_required()
def update_instructor(request, instructor_id):
    instructor_being_updated = get_object_or_404(Instructor, pk=instructor_id)
    
    if request.method == 'POST':
        instructor_form = InstructorProfile(request.POST, instance=instructor_being_updated)

        if instructor_form.is_valid():
            instructor_form.save()
            return redirect(reverse('view_instructors'))

        else:
            return render(request, 'lessons/update_instructor.html', {
                'instructor_form': instructor_form
            })

    else:
        instructor_form = InstructorProfile(instance=instructor_being_updated)
        return render(request, 'lessons/update_instructor.html', {
            'instructor_form': instructor_form,
            'instructor': instructor_being_updated
        })

@permission_required('lessons.delete_instructor', raise_exception=True)
@login_required()
def delete_instructor(request, instructor_id):
    instructor = Instructor.objects.all()
    instructor_to_delete = get_object_or_404(Instructor, pk=instructor_id)
    if request.method == 'POST':
        instructor_to_delete.delete()
        return redirect('view_instructors')
    else:
        return render(request, 'lessons/delete_instructor.html', {
            'instructor': instructor_to_delete,
        })


# About Forum

def view_forum_public(request):
    forum = Forum.objects.all()
    search_forum = SearchForm(request.GET)

    if request.GET:
        query = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query & Q(title__icontains=title)

        forum = forum.filter(query)
        return render(request, 'lessons/view_forum_public.html', {
            'forum': forum,
            'search_forum': search_forum
        })
    else:
        lessons = Lesson.objects.all()
        return render(request, 'lessons/view_forum_public.html', {
            'search_forum': search_forum,
            'forum': forum
        })

@login_required()
def view_forum(request):
    forum = Forum.objects.all()
    search_forum = SearchForm(request.GET)

    if request.GET:
        query = ~Q(pk__in=[])

        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query & Q(title__icontains=title)

        forum = forum.filter(query)
        return render(request, 'lessons/view_forum.html', {
            'forum': forum,
            'search_forum': search_forum
        })
    else:
        lessons = Lesson.objects.all()
        return render(request, 'lessons/view_forum.html', {
            'search_forum': search_forum,
            'forum': forum
        })


def create_forum_public(request):
    if request.method == 'POST':
        create_forum = AddForum(request.POST)
        if create_forum.is_valid():
            create_forum.save()
            return redirect('view_forum_public')
        else:
            return render(request, 'lessons/create_forum_public.html', {
                'create_forum': create_forum
            })
    else:
        create_forum = AddForum()
        return render(request, 'lessons/create_forum_public.html', {
            'create_forum': create_forum
        })
        
@login_required()
def create_forum(request):
    if request.method == 'POST':
        create_forum = AddForum(request.POST)
        if create_forum.is_valid():
            create_forum.save()
            return redirect('view_forum')
        else:
            return render(request, 'lessons/create_forum.html', {
                'create_forum': create_forum
            })
    else:
        create_forum = AddForum()
        return render(request, 'lessons/create_forum.html', {
            'create_forum': create_forum
        })

@permission_required('lessons.delete_forum', raise_exception=True)
@login_required()
def delete_forum(request, forum_id):
    forum = Forum.objects.all()
    forum_to_delete = get_object_or_404(Forum, pk=forum_id)
    if request.method == 'POST':
        forum_to_delete.delete()
        return redirect('view_forum')
    else:
        return render(request, 'lessons/delete_forum.html', {
            'forum': forum_to_delete,
        })

@login_required()
def forum_details(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    return render(request, 'lessons/forum_details.html', {
        'forum':forum
    })

def forum_details_public(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    return render(request, 'lessons/forum_details_public.html', {
        'forum':forum
    })

@permission_required('lessons.create_comment', raise_exception=True)
@login_required()
def create_comment(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    if request.method == 'POST':
        form = AddComment(request.POST)
        comment = form.save(commit=False)
        comment.thread = forum
        comment.commentor = request.user
        comment.save()
        return redirect('view_forum')

    else:
        form = AddComment
        return render(request, 'lessons/create_comment.html', {
            'form':form,
            'forum': forum
        })


@permission_required('lessons.delete_comment', raise_exception=True)
@login_required()
def delete_comment(request, comment_id):
    comment = Comment.objects.all()
    comment_to_delete = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment_to_delete.delete()
        return redirect('view_forum')
    else:
        return render(request, 'lessons/delete_comment.html', {
            'comment': comment_to_delete
        })


@permission_required('lessons.update_comment', raise_exception=True)
@login_required()
def update_comment(request, comment_id):
    comment_being_updated = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        comment_form = AddComment(request.POST, instance=comment_being_updated)

        if comment_form.is_valid():
            comment_form.save()
            return redirect('view_forum')
        else:
            return render(request, 'lessons/update_comment.html')
    else:
        comment_form = AddComment(instance=comment_being_updated)
        return render(request, 'lessons/update_comment.html', {
            'form': comment_form
        })