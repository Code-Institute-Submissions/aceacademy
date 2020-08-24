from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(blank=False, max_length=100)
    code = models.CharField(blank=False, max_length=100)
    desc = models.TextField(blank=False)
    cover = CloudinaryField()

    def __str__(self):
        return self.title 