import django.forms as forms

# import in the review model
from .models import Forum, Comment


class ForumForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'date')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)