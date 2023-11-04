from django.test import TestCase
from cookingblog.forms import CommentForm, CookingRecipePostCreateForm, CookingRecipePostUpdateForm


class TestCommentForm(TestCase):
    """Test CommentForm"""

    def test_commentform_fields(self):
        form = CommentForm()
        self.assertTrue(form.fields['body'])
    

    def test_commentform_with_valid_data(self):
        """test Commentform with valid data"""
        form = CommentForm(data={
            'body': 'test comment',
        })
        self.assertTrue(form.is_valid())