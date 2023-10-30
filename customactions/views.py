from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import (CreateView, DetailView, UpdateView)
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ProfileForm
from .models import Profile


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