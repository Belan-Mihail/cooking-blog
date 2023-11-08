from django.test import TestCase
from cookingblog.models import CookingRecipePost, Comment, Category
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class TestCookingRecipePostModel(TestCase):
    """
    Test for CookingRecipePost Model
    """
    def setUp(self):
        """ Create testing post """
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
        Check test model belongs CookingRecipePost Model 
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


class TestCommentModel(TestCase):
    """
    Test for Comment Model
    """
    def setUp(self):
        """ Create testing post and comment"""
        Category.objects.create(name='soups',),
        User.objects.create(username='admin',),
        self.post = CookingRecipePost.objects.create(
            cooking_recipe_title="post 1",
            cooking_recipe_author_id=1,
            cooking_recipe_body = "content",
            cat_id=1,
        )
        self.com = Comment.objects.create(
            cooking_recipe_post=self.post,
            name='John',
            email='test@gmail.com',
            body='test',
        )


    def test_comment_str(self):
        """
        Checks str for Comment Model
        """
        obj = self.com
        self.assertEqual(str(obj), "Comment test by John")
    

    def test_checking_object_comment(self):
        """
        Check test model belongs Comment Model 
        """
        obj = self.com
        self.assertTrue(isinstance(obj, Comment))
    

    def test_comment_has_correctly_name(self):
        """
        Check comment name correctly
        """
        obj = self.com
        self.assertEqual(obj.name, 'John')


class TestCategoryModel(TestCase):
    """
    Test for Category Model
    """
    def setUp(self):
        """ Create testing category """
        self.categor = Category.objects.create(name='soups', slug='soups')
    

    def test_category_str(self):
        """
        Checks str for Category Model
        """
        obj = self.categor
        self.assertEqual(str(obj), "soups")
    

    def test_checking_object_category(self):
        """
        Check test model belongs Category Model 
        """
        obj = self.categor
        self.assertTrue(isinstance(obj, Category))
    

    def test_get_absolute_url_category(self):
        """
        Checks get_absolute_url for Category Model
        """
        obj = self.categor
        self.assertEqual(obj.get_absolute_url(), '/category/soups/')
    

    def test_category_has_correctly_name(self):
        """
        Check category name correctly
        """
        obj = self.categor
        self.assertEqual(obj.name, 'soups')