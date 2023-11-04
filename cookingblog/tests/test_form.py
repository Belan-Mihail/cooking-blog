from django.test import TestCase
from cookingblog.forms import CommentForm, CookingRecipePostCreateForm, CookingRecipePostUpdateForm


class TestCommentForm(TestCase):
    """Test CommentForm"""

    def test_form_fields(self):
        form = CommentForm()
        self.assertTrue(form.fields['body'])