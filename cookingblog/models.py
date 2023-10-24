from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Field status from CookingRecipeModel
STATUS = ((0, "Draft"), (1, "Published"))

class CookingRecipePost(models.Model):
    """
    Model for posts
    """
    cooking_recipe_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    cooking_recipe_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cooking_recipe_blog_posts"
    )
    cooking_recipe_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    cooking_recipe_body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='cookingrecipepost_like', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name="categories")
    

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "recipe"
        verbose_name_plural = "recipes"

    def __str__(self):
        return self.cooking_recipe_title


    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for comments
    """
    cooking_recipe_post = models.ForeignKey(CookingRecipePost, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["id"]
        verbose_name = "category"
        verbose_name_plural = "categories"
