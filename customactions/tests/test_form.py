from django.test import TestCase
from customactions.forms import ProfileForm, ContactForm
from django.core.files.uploadedfile import SimpleUploadedFile
from customactions.models import Profile
from django.contrib.auth.models import User

class TestProfileForm(TestCase):
    """Test ProfileForm"""

    def test_profileform_fields(self):
        """
        test ProfileForm fields
        """
        form = ProfileForm()
        self.assertIn("nickname", form.fields)
        self.assertIn("avatar", form.fields)
        self.assertIn("bio", form.fields)
        self.assertIn("birth_date", form.fields)
        self.assertIn("region", form.fields)
        self.assertIn("occupation", form.fields)


    def test_profileform_with_valid_data(self):
        """test ProfileForm with valid data"""
        form = ProfileForm(data={
            'nickname': 'test nickname',
            'avatar': SimpleUploadedFile("image.jpg", b"file data"),
            'bio': 'test',
            'birth_date': '1988-08-14',
            'region': 'test-region',
            'occupation': 'test-occupation'

        })
        self.assertTrue(form.is_valid())
    

    def test_profileform_with_invalid_data(self):
        """test ProfileForm with invalid data"""
        form = ProfileForm(data={
            'nickname': 'test nickname',
            'avatar': SimpleUploadedFile("image.jpg", b"file data"),
            'bio': 'test',
            # add invilid format of birth_date
            'birth_date': '14-08-1988',
            'region': 'test-region',
            'occupation': 'test-occupation'

        })
        self.assertFalse(form.is_valid())


    def test_profileform_invalid_format_of_birth_date(self):
        """test ProfileForm with invalid data"""
        form = ProfileForm(data={
            # add invilid format of birth_date
            'birth_date': '1988-08-41',
        })
        self.assertFalse(form.is_valid())
    

# class TestCookingRecipePostCreateForm(TestCase):
#     """Test CookingRecipePostCreateForm"""

    

# def test_commentform_fields(self):
    #     form = CommentForm()
    #     self.assertTrue(form.fields['body'])
    

    # def test_commentform_with_valid_data(self):
    #     """test Commentform with valid data"""
    #     form = CommentForm(data={
    #         'body': 'test comment',
    #     })
    #     self.assertTrue(form.is_valid())
    

    # def test_commentform_with_invalid_data(self):
    #     """test Commentform with invalid data"""
    #     form = CommentForm(data={})
    #     self.assertFalse(form.is_valid())


# class CookingRecipePostUpdateForm(TestCase):
#     """Test CookingRecipePostUpdateForm"""

#     def test_cookingrecipepostupdateform_fields(self):
#         form = CookingRecipePostCreateForm()
#         self.assertIn("cooking_recipe_title", form.fields)
#         self.assertIn("cat", form.fields)
#         self.assertIn("cooking_recipe_image", form.fields)
#         self.assertIn("excerpt", form.fields)
#         self.assertIn("cooking_recipe_body", form.fields)
    

#     def test_cookingrecipepostupdateform_with_invalid_data(self):
#         """test CookingRecipePostUpdateForm with invalid data"""
#         form = CookingRecipePostCreateForm(data={})
#         self.assertFalse(form.is_valid())
    

#     def test_cookingrecipepostupdateform_is_not_cookingrecipepostcreateform(self):
#         """
#         test CookingRecipePostUpdateForm  is not CookingRecipePostCreateForm
#         """
#         form = CookingRecipePostUpdateForm()
#         self.assertFalse(isinstance(form, CookingRecipePostCreateForm))