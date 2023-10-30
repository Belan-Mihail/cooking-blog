from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'avatar', 'bio', 'birth_date', 'region', 'occupation')
    list_filter = ('nickname',)
    search_fields = ('nickname', 'bio')