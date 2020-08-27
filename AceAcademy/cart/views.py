from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Q
from datetime import date

from lessons.models import *
from .forms import *

from accounts.views import *
from accounts.forms import CreateUserForm
from accounts.decorators import unauthenticated_user, allowed_users, admin_only

def add_to_cart(request, lesson_id):
    cart = request.session.get('shopping_cart', {})
    
    if lesson_id not in cart:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        cart[lesson_id] = {
            'id':lesson_id,
            'title': lesson.title,
            'cost': 99,
            'qty': 1
        } 
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Lesson has been added to your cart!")
        return redirect(reverse('home'))
    else:
        cart[lesson_id]['qty'] +=1
        request.session['shopping_cart'] = cart
        return redirect(reverse('home'))