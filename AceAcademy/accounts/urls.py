from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('main/', views.user_main, name="user_main"),
    path('admin/', views.admin_main, name="admin_main")
]