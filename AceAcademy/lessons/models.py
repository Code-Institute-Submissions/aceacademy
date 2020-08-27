from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Instructor(models.Model):
    instructor_full_name = models.CharField(blank=False, max_length=100, validators=[MinLengthValidator(3)])
    instructor_preferred_name = models.CharField(blank=False, max_length=100)
    years_experience = models.IntegerField(blank=False)
    instructor_mobile_number = PhoneNumberField(blank=False)
    qualifications = models.TextField(blank=False)

    def __str__(self):
        return self.instructor_preferred_name

class Reviews(models.Model):
    lesson_reviewed = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review_content = models.TextField(blank=False)
    review_date = models.DateField(blank=False)
    rating = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.review_content
        
class Lesson(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    cost = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    syllabus = models.CharField(blank=False, max_length=100)
    tags = models.CharField(blank=False, max_length=100)
    education_level = models.CharField(blank=False, max_length=100)
    cover = CloudinaryField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


