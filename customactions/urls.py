from django.urls import path
from . import views
from .views import CreateProfileView, ProfilePageView


urlpatterns = [
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('profile_page/', views.ProfilePageView.as_view(), name='profile_page'),

]