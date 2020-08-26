from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator

# Create your models here.

class Instructor(models.Model):
    instructor_full_name = models.CharField(blank=False, max_length=100)
    instructor_preferred_name = models.Charfield(blank=False, max_length=100)
    years_experience = models.IntegerField(blank=False)
    instructor_mobile_number = PhoneNumberField(blank=False)
    qualifications = models.TextField(blank=False)

    def __str__(self):
        return self.instructor_preferred_name + " with " + self.years_experience + " of experience"

class Reviews(models.Model):
    lesson_reviewed = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review_content = models.textField(blank=False)
    review_date = models.DateField(blank=False)
    rating = models.IntegerField(blank=False)

    def __str__(self):
        return self
        
class Lesson(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.CharField(blank=False, max_length=255)
    cost = MoneyField(max_digits=5, decimal_places=2, blank=False, default_currency='SGD')
    syllabus = models.CharField(blank=False, max_lenght=100)
    tags = models.CharField(blank=False, max_lenght=100)
    education_level = models.CharField(blank=False, max_lenght=100)
    cover = CloudinaryField()
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return self


