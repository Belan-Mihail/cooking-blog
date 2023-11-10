from django.urls import path
from . import views
from .views import CreateProfileView, ProfilePageView, UpdateProfile, contact


urlpatterns = [
    path(
        'create_profile/',
        CreateProfileView.as_view(),
        name='create_profile'
    ),
    path(
        'profile_page/',
        views.ProfilePageView.as_view(),
        name='profile_page'
    ),
    path('update_profile/', UpdateProfile.as_view(), name='update_profile'),
    path('contact/', contact, name='contact'),
]
