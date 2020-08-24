from django.contrib import admin
from django.urls import path, include
import cart.views

urlpatterns = [
    path('add/<lesson_id>', cart.views.add_to_cart)
]