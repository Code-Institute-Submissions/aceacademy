from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q

from .models import *
from .forms import *

from accounts.views import *
from accounts.forms import CreateUserForm
from accounts.decorators import unauthenticated_user, allowed_users, admin_only


def forum(request):
    return render(request, 'forum/forum.html')