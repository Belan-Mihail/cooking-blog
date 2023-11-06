from django.test import TestCase, Client
from cookingblog.models import CookingRecipePost, Comment, Category
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory
from cookingblog.views import CookingRecipesPostList, CookingRecipePostDetail


class TestView(TestCase):
    """
    Class for test views
    """
    def setUp(self):
        Category.objects.create(name='soups', slug='soups'),
        User.objects.create(username='admin',),
        self.post = CookingRecipePost.objects.create(
            cooking_recipe_title="post 1",
            slug='post_1',
            cooking_recipe_author_id=1,
            cooking_recipe_body = "content",
            cat_id=1,
            status=1,
            
            
            )
        self.com = Comment.objects.create(
            cooking_recipe_post=self.post,
            name='John',
            email='test@gmail.com',
            body='test',
        )
    

    def test_home_page_used_template(self):
        """
        This tests display of the home page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')
        self.assertTrue('categories' in response.context)
    

    # def test_(self):
    #     request = RequestFactory().get('/')
    #     view = CookingRecipesPostList.as_view(template_name = "index.html")
    #     response = view(request)
    #     self.assertEqual(response.status_code, 200)



    def test_detail_page_used_template(self):
        """
        This tests display of the post detail page
        """
        
        post = self.post
        
        response = self.client.get(reverse('cooking_recipe_post_detail', kwargs={'slug': self.post.slug}))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        
    

    def test_create_post_used_template(self):
        """
        This tests display of the create_post page
        """
        response = self.client.get(reverse('recipe_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_create.html', 'base.html')


    # def test_update_page_used_template(self):
    #     """
    #     This tests display of the post detail page
    #     # """
        
    #     login = self.client.login(username='admin', password='abc564!')
    #     post = self.post
    #     response = self.client.get(reverse('recipe_update', kwargs={'slug': self.post.slug}))
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'recipe_update.html')
        
    

    