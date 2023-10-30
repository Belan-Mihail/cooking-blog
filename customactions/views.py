from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import (CreateView, DetailView, UpdateView)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ProfileForm
from .models import Profile
from cookingblog.models import CookingRecipePost


class CreateProfileView(SuccessMessageMixin, CreateView):
    """
    A class view to create
    user profile
    """
    model = Profile
    form_class = ProfileForm
    success_url = '/'
    template_name = 'customactions/create_profile.html'
    success_message = 'Your profile has been created successfully!'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfilePageView(DetailView):
    """
    A class view to see detail
    of user profile
    """
    model = Profile
    template_name = 'profile_page.html'
    
    
    def get_object(self, *args, **kwargs):
        return self.request.user


    def get_context_data(self,**kwargs):
        context = super(UserProfilePageView, self).get_context_data(**kwargs)
        context['cooking_recipes_post'] = CookingRecipePost.objects.filter(status=1).order_by("-created_on")
        return context