from django import forms
from .models import Lesson, Instructor, Reviews, Forum, Comment
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
        fields = ('instructor_full_name', 'instructor_preferred_name', 'cover', 'years_experience', 
                'instructor_mobile_number', 'qualifications')
    cover = CloudinaryJsFileField()

class AddReview(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('review_content', 'rating')

class AddForum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('thread_title', 'thread_content', 'tags', 'education_level', 'full_name', 'email_address')

class AddComment(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('content',)

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

class SearchInstructor(forms.Form):
    instructor_full_name = forms.CharField(max_length=100, required=False)
