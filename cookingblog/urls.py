from . import views
from django.urls import path


urlpatterns = [
    path("", views.CookingRecipesPostList.as_view(), name="home"),
    path('<slug:slug>/', views.CookingRecipePostDetail.as_view(), name='cooking_recipe_post_detail'),
]