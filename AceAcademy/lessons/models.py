from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.
education_level = (
    ('Lower Primary','Lower Primary'),
    ('Upper Primary', 'Upper Primary'),
    ('Lower Secondary','Lower Secondary'),
    ('Upper Secondary','Upper Secondary'),
    ('Junior College','JC')
)

syllabus = (
    ('PSLE','PSLE'),
    ('O Level', 'GCSE O Level'),
    ('A Level','GCSE A Level')
)

tags = (
    ('Primary Math','Primary Mathematics'),
    ('Additional Math', 'Additional Mathematics'),
    ('Elementary Math','Elementary Mathematics'),
    ('H1 Math', 'H1 Mathematics'),
    ('H2 Math', 'H2 Mathematics')
)

class Instructor(models.Model):
    instructor_full_name = models.CharField(blank=False, max_length=100, validators=[MinLengthValidator(3)])
    instructor_preferred_name = models.CharField(blank=False, max_length=100)
    years_experience = models.IntegerField(blank=False)
    instructor_mobile_number = PhoneNumberField(blank=False)
    qualifications = models.TextField(blank=False)
    cover = CloudinaryField(blank=False)

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
    cost = models.DecimalField(blank=False, max_digits=10, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    syllabus = models.CharField(blank=False, choices=syllabus, default='A Level', max_length=100)
    tags = models.CharField(blank=False, choices=tags, default='H2 Math', max_length=100)
    education_level = models.CharField(blank=False, default='Junior College', choices=education_level,  max_length=100)
    cover = CloudinaryField(blank=False)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Forum(models.Model):
    thread_title = models.CharField(blank=False, max_length=255)
    thread_content = models.TextField(blank=False)
    full_name = models.CharField(blank=False, max_length=255)
    tags = models.CharField(blank=False, choices=tags, default='H2 Math', max_length=100)
    education_level = models.CharField(blank=False, default='Junior College', choices=education_level,  max_length=100)
    email_address = models.EmailField(blank=False, max_length=254)

    def __str__(self):
        return self.thread_title

class Comment(models.Model):
    thread = models.ForeignKey('Forum', on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    commentor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.content



