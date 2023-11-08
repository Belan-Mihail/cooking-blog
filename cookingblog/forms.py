from .models import Comment, CookingRecipePost
from django import forms



class CommentForm(forms.ModelForm):
    """
    Form for Comments model
    """
    class Meta:
        model = Comment
        fields = ('body',)


class CookingRecipePostCreateForm(forms.ModelForm):
    """
    Form for posting posts on the site
    """
    class Meta:
        model = CookingRecipePost
        fields = ('cooking_recipe_title', 'cat', 'cooking_recipe_image', 'excerpt', 'cooking_recipe_body')


class CookingRecipePostUpdateForm(forms.ModelForm):
    """
    Form for update posts on the site
    """
    class Meta:
        model = CookingRecipePost
        fields = ('cooking_recipe_title', 'cat', 'cooking_recipe_image', 'excerpt', 'cooking_recipe_body')


