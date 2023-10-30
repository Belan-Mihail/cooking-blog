from django.contrib import admin

from .models import Profile, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'avatar', 'bio', 'birth_date', 'region', 'occupation')
    list_filter = ('nickname',)
    search_fields = ('nickname', 'bio')


@admin.register(Contact)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ('name',)
    search_fields = ('name', 'message')