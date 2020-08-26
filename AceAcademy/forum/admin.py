from django.contrib import admin
from .models import Thread, Comments

# Register your models here.
admin.site.register(Thread)
admin.site.register(Comments)