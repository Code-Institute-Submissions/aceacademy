import django.forms as forms

# import in the review model
from .models import Thread, Comments


class ForumForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('thread_title',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_content',)