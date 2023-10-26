from .models import Comment
from django import forms
from .models import CookingRecipePost


class CommentForm(forms.ModelForm):
    """
    Form for comments
    """
    class Meta:
        model = Comment
        fields = ('body',)