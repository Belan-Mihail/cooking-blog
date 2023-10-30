from django.urls import path
from . import views
from .views import CreateProfileView


urlpatterns = [
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),

]