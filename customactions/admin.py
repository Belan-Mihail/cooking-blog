from django.contrib import admin
from .models import Profile, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Registration Profile model in admin,
    add filters and displaying fields
    """
    list_display = (
        'nickname', 'avatar', 'bio', 'birth_date', 'region', 'occupation'
    )
    list_filter = ('nickname',)
    search_fields = ('nickname', 'bio')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Registration Contact model in admin,
    add filters and displaying fields
    """
    list_display = ('name', 'email', 'message')
    list_filter = ('name',)
    search_fields = ('name', 'message')
