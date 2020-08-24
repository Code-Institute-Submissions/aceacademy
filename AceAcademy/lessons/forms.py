from django import forms
from .models import Lesson
from django.db.models import Q

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'code', 'desc')

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
