from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import CookingRecipePost
from .forms import (
    Comment, 
    CommentForm,
    CookingRecipePostCreateForm
) 
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin



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
    """
    View for displaying a single post
    """
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
                "commented": False,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = CookingRecipePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.cooking_recipe_post = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "slug": slug,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """
    View for add or remove likes
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(CookingRecipePost, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('cooking_recipe_post_detail', args=[slug]))


class CookingRecipePostCreateView(SuccessMessageMixin, CreateView):
    """
    View for create new post
    """
    model = CookingRecipePost
    template_name = 'recipe_create.html'
    form_class = CookingRecipePostCreateForm
    success_url = '/'
    success_message = 'Your recipe is is awaiting administrator approval'


    def form_valid(self, form):
        form.instance.cooking_recipe_author = self.request.user
        form.save()
        return super().form_valid(form)
