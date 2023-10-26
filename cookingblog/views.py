from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import CookingRecipePost
from .forms import Comment, CommentForm


class CookingRecipesPostList(generic.ListView):
    """
    View for displaying a list of posts
    """
    model = CookingRecipePost
    queryset = CookingRecipePost.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 5
    context_object_name = 'cooking_recipes_post_list'


class CookingRecipePostDetail(View):

    model = CookingRecipePost

    def get(self, request, slug, *args, **kwargs):
        queryset = CookingRecipePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )