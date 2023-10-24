from django.shortcuts import render
from django.views import generic
from .models import CookingRecipePost


class CookingRecipesPostList(generic.ListView):
    """
    View for displaying a list of posts
    """
    model = CookingRecipePost
    queryset = CookingRecipePost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 5
    context_object_name = 'cooking_recipes_post_list'