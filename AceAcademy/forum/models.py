from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Comments(models.Model):
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    comment_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateField(blank=False)
    comment_content = models.TextField(blank=False)

    def __str__(self):
        return self


class Thread(models.Model):
    thread_title = models.CharField(blank=False, max_length=255)
    thread_date = models.DateField(blank=False)
    thread_content = models.TextField(blank=False)
    thread_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text[0:50]
