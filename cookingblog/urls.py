from . import views
from django.urls import path
from .views import (
    CookingRecipePostCreateView,
    CookingRecipePostUpdateView
)


urlpatterns = [
    path("", views.CookingRecipesPostList.as_view(), name="home"),
    path('<slug:slug>/', views.CookingRecipePostDetail.as_view(), name='cooking_recipe_post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('recipe/create/', CookingRecipePostCreateView.as_view(), name='recipe_create'),
    path('recipe/<slug:slug>/update/', CookingRecipePostUpdateView.as_view(), name='recipe_update'),
]