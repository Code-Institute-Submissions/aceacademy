from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.

def homepage(request):
    return render(request, 'main/index.html')