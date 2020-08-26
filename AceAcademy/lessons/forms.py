from django import forms
from .models import Lesson, Instructor, Reviews
from django.db.models import Q
from cloudinary.forms import CloudinaryJsFileField


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'desc', 'cover', 'cost', 'syllabus', 'tags',
                    'tags', 'education_level', 'instructor')
        
    cover = CloudinaryJsFileField()

class InstructorProfile(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ('instructor_full_name', 'instructor_preferred_name', 'years_experience', 
                'instructor_mobile_number', 'qualifications')

class AddReview(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('lesson_reviewed', 'reviewer', 'review_content', 'review_date', 'rating')

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
