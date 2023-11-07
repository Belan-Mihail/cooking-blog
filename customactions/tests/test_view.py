from django.test import TestCase, Client
from customactions.models import Profile, Contact
from django.contrib.auth.models import User
from django.urls import reverse


class TestView(TestCase):
    """
    Class for test views
    """
    def setUp(self):
        User.objects.create(username='admin', password='abc564!'),
        self.profile = Profile.objects.create(
            nickname="administrator",
            bio='bio',
            user_id=1,
            region = "Germany",
            occupation='developper',
    )