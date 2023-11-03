from django.test import TestCase
from cookingblog.models import CookingRecipePost, Comment, Category
from django.contrib.auth.models import User


class TestCookingRecipePostModel(TestCase):
    """
    Test for CookingRecipePost Model
    """
    def setUp(self):
        post = CookingRecipePost.objects.create(
            cooking_recipe_title="post 1",
            cooking_recipe_author="admin",
            cooking_recipe_body = "content",
            )


    def test_1(self):
        
        data = self.post
        self.assertTrue(isinstance(data, CookingRecipePost))

    # @classmethod
    # def setUpTestData(cls):
    #     #Set up non-modified objects used by all test methods
    #     Author.objects.create(first_name='Big', last_name='Bob')