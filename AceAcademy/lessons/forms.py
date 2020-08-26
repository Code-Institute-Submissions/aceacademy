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

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
