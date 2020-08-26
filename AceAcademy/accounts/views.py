from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


# Create your views here.
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
            messages.success(request, 'Account was created for ' + first_name)
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
            return redirect('user_main')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'See you soon!')
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def user_main(request):
    return render(request, 'accounts/user_index.html')

@login_required(login_url='login')
def admin_main(request):
    return render(request, 'accounts/admin_index.html')