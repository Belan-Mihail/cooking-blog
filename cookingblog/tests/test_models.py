from django.test import TestCase
from cookingblog.models import CookingRecipePost, Comment, Category
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class TestCookingRecipePostModel(TestCase):
    """
    Test for CookingRecipePost Model
    """
    def setUp(self):
        Category.objects.create(name='soups',),
        User.objects.create(username='admin',),
        self.post = CookingRecipePost.objects.create(
            cooking_recipe_title="post 1",
            cooking_recipe_author_id=1,
            cooking_recipe_body = "content",
            cat_id=1,
            )


    def test_checking_object(self):
        """
        Check test model belongs CookingRecipePost Model class
        """
        obj = self.post
        self.assertTrue(isinstance(obj, CookingRecipePost))


    def test_post_has_correctly_slug(self):
        """
        Check slugs correctly
        """
        obj = self.post
        self.assertEqual(obj.slug, slugify(obj.cooking_recipe_title))


    def test_post_has_correctly_title(self):
        """
        Check title correctly
        """
        obj = self.post
        self.assertEqual(obj.cooking_recipe_title, 'post 1')
    

    def test_post_str(self):
        """
        Checks str for CookingRecipePost Model
        """
        obj = self.post
        self.assertEqual(str(obj), "post 1")
    

    def test_get_absolute_url(self):
        """
        Checks get_absolute_url for CookingRecipePost Model
        """
        obj = self.post
        self.assertEqual(obj.get_absolute_url(), '/post-1/')

    def test_post_has_correctly_category_name(self):
        """
        Check category name correctly
        """
        obj = self.post
        self.assertEqual(obj.cat.name, 'soups')