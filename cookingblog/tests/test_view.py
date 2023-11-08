from django.test import TestCase, Client
from cookingblog.models import CookingRecipePost, Comment, Category
from django.contrib.auth.models import User
from django.urls import reverse



class TestView(TestCase):
    """
    Class for test views cookingblog app
    """
    def setUp(self):
        """ Create testing post with comment and category"""
        Category.objects.create(name='soups', slug='soups'),
        self.user = User.objects.create_user(username='admin', password='abc564!')
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
        
    

    def test_cookingrecipespostlist_status_and_used_template(self):
        """
        This tests check status code and used template CookingRecipesPostList
        and check context object name in response.context
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')
        self.assertTrue('cooking_recipes_post_list' in response.context)
    

    def test_cookingrecipepostdetail_status_and_used_template(self):
        """
        This tests check status code 
        and used template CookingRecipePostDetail
        """
        post = self.post
        response = self.client.get(
            reverse('cooking_recipe_post_detail', kwargs={'slug': self.post.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        
    

    def test_cookingrecipepostcreate_status_and_used_template(self):
        """
        This tests check status code 
        and used template CookingRecipePostCreateView
        """
        login = self.client.login(username='admin', password='abc564!')
        response = self.client.get(reverse('recipe_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_create.html', 'base.html')


    def test_cookingrecipepostupdate_status_and_used_template(self):
        """
        This tests check status code 
        and used template CookingRecipePostUpdateView
        """
        login = self.client.login(username='admin', password='abc564!')
        self.assertTrue(login)
        post = self.post
        response = self.client.get(reverse('recipe_update', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_update.html', 'base.html')
    

    def test_cookingrecipepostdelete_status_and_used_template(self):
        """
        This tests check status code 
        and used template CookingRecipePostDeleteView
        """
        login = self.client.login(username='admin', password='abc564!')
        self.assertTrue(login)
        post = self.post
        response = self.client.get(reverse('recipe_delete', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_delete.html', 'base.html')

    
    def test_cookingrecipepostcategory_status_and_used_template(self):
        """
        This tests check status code 
        and used template CookingRecipePostCategory
        """
        post = self.post
        response = self.client.get(reverse('selectedcategory', args=[self.post.cat.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')
    

    def test_deletemycomment_status_and_redirect(self):
        """
        This tests check status code 
        and correctly redirect deletemycomment
        """
        response = self.client.get(reverse('commentdelete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse(
                'cooking_recipe_post_detail', kwargs={'slug': self.post.slug}
            )
        )
    

    def test_postlike_status_and_redirect(self):
        """
        This tests check status code 
        and correctly redirect PostLike
        """
        login = self.client.login(username='admin', password='abc564!')
        self.assertTrue(login)
        post = self.post
        response = self.client.post(reverse('post_like', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('cooking_recipe_post_detail', args=[self.post.slug]))
    

    




        
    

    