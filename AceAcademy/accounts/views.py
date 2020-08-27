from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q

# from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
# from lessons.models import Lesson
# from lessons.forms import LessonForm


# Regarding user authentication
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(request, 'Account was created, see you inside!')
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('index')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'See you soon!')
    return redirect('login')

# Homepage

@login_required(login_url='login')
# @allowed_users(allowed_roles=['user'])
def index(request):
    return render(request, 'accounts/index.html')

# For Admin
# def create_lesson(request):
#     if request.method == 'POST':
#         create_lesson = LessonForm(request.POST)
#         print(request.POST)
#         if create_lesson.is_valid():
#             create_lesson.save()
#             messages.success(request, f"New lesson has been created!")
#             return redirect(reverse(index))
#         else:
#             return render(request, 'lessons/create_lesson.html', {
#                 'form': create_lesson
#             })
#     else:
#         create_lesson = LessonForm()
#         return render(request, 'lessons/create_lesson.html', {
#             'form': create_lesson
#         })


# For User
