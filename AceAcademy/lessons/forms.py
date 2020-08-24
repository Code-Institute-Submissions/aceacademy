from django import forms
from .models import Lesson
from django.db.models import Q
from cloudinary.forms import CloudinaryJsFileField


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'code', 'desc', 'cover')
        
    cover = CloudinaryJsFileField()

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
