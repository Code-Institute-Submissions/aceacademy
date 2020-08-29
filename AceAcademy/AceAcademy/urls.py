"""AceAcademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lessons import views
import lessons.urls, cart.urls, checkout.urls

urlpatterns = [
    path('', lessons.views.home,
        name="home"),
    path('browse/', lessons.views.view_lessons_public,
        name="view_lessons_public"),
    path('instructors/', lessons.views.view_instructors_public,
        name="view_instructors_public"),
    path('forum/', lessons.views.view_forum_public,
        name="view_forum_public"),

    path('forum/create/', lessons.views.create_forum_public,
        name="create_forum_public"),
    path('forum/<forum_id>/comments/', lessons.views.forum_details_public,
        name="forum_details_public"),

    path('admin/', admin.site.urls),

    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('accounts/', include('allauth.urls')),
    path('lessons/', include('lessons.urls'))

]
