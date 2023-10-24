from django.contrib import admin
from .models import CookingRecipePost, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(CookingRecipePost)
class CookingRecipePostAdmin(SummernoteModelAdmin):
    """
    Registration CookingRecipePost model in admin, add filters and displaying fields
    """
    summernote_fields = ('cooking_recipe_body')
    list_display=('cooking_recipe_title', 'slug', 'status')
    



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Registration Comment model in admin, add filters and displaying fields
    """
    list_display = ('name', 'body', 'cooking_recipe_post', 'created_on', 'approved')
    

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Registration Category model in admin, add filters and displaying fields
    """
    list_display = ('name', 'slug', 'id')
    prepopulated_fields = {"slug": ("name", )}


