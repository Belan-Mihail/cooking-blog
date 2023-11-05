from django.test import TestCase
from cookingblog.forms import CommentForm, CookingRecipePostCreateForm, CookingRecipePostUpdateForm
from django.core.files.uploadedfile import SimpleUploadedFile
from cookingblog.models import Category

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
    

    def test_commentform_with_invalid_data(self):
        """test Commentform with invalid data"""
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())


class TestCookingRecipePostCreateForm(TestCase):
    """Test CookingRecipePostCreateForm"""

    def test_cookingrecipepostcreateform_fields(self):
        form = CookingRecipePostCreateForm()
        self.assertIn("cooking_recipe_title", form.fields)
        self.assertIn("cat", form.fields)
        self.assertIn("cooking_recipe_image", form.fields)
        self.assertIn("excerpt", form.fields)
        self.assertIn("cooking_recipe_body", form.fields)


    def test_cookingrecipepostcreateform_with_valid_data(self):
        """test CookingRecipePostCreateForm with valid data"""
        cat1 = Category.objects.create(name='soups',)
        form = CookingRecipePostCreateForm(data={
            'cooking_recipe_title': 'test title',
            'cat':cat1,
            'cooking_recipe_image': SimpleUploadedFile("image.jpg", b"file data"),
            'excerpt': 'test',
            'cooking_recipe_body': 'content',

        })
        self.assertTrue(form.is_valid())
    

    def test_cookingrecipepostcreateform_with_invalid_data(self):
        """test CookingRecipePostCreateForm with invalid data"""
        form = CookingRecipePostCreateForm(data={})
        self.assertFalse(form.is_valid())
    

    def test_cookingrecipepostcreateform_is_not_cookingrecipepostupdateform(self):
        """
        test CookingRecipePostCreateForm is not CookingRecipePostUpdateForm
        """
        form = CookingRecipePostCreateForm()
        self.assertFalse(isinstance(form, CookingRecipePostUpdateForm))


class CookingRecipePostUpdateForm(TestCase):
    """Test CookingRecipePostUpdateForm"""

    def test_cookingrecipepostupdateform_fields(self):
        form = CookingRecipePostCreateForm()
        self.assertIn("cooking_recipe_title", form.fields)
        self.assertIn("cat", form.fields)
        self.assertIn("cooking_recipe_image", form.fields)
        self.assertIn("excerpt", form.fields)
        self.assertIn("cooking_recipe_body", form.fields)


    def test_cookingrecipepostupdateform_with_invalid_data(self):
        """test CookingRecipePostUpdateForm with invalid data"""
        form = CookingRecipePostCreateForm(data={})
        self.assertFalse(form.is_valid())
    

    def test_cookingrecipepostupdateform_is_not_cookingrecipepostcreateform(self):
        """
        test CookingRecipePostUpdateForm  is not CookingRecipePostCreateForm
        """
        form = CookingRecipePostUpdateForm()
        self.assertFalse(isinstance(form, CookingRecipePostCreateForm))