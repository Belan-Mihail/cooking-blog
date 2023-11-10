from django.test import TestCase, Client
from customactions.models import Profile, Contact
from django.contrib.auth.models import User
from django.urls import reverse


class TestView(TestCase):
    """
    Class for test views
    """
    def setUp(self):
        """
        Create test model
        """
        self.user = User.objects.create_user(username='admin', password='abc564!')
        self.profile = Profile.objects.create(
            nickname="administrator",
            bio='bio',
            user_id=1,
            region = "Germany",
            occupation='developper',
    )

    def test_create_profile_used_template(self):
        """
        This tests check status code 
        and used template CreateProfileView
        """
        response = self.client.get(reverse('create_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'customactions/create_profile.html' in (t.name for t in response.templates))
        self.assertTrue(response, 'base.html' in (t.name for t in response.templates))
    

    def test_view_profile_used_template(self):
        """
        This tests check status code 
        and used template ProfilePageView
        """
        response = self.client.get(reverse('profile_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'customactions/profile_page.html' in (t.name for t in response.templates))
        self.assertTrue(response, 'base.html' in (t.name for t in response.templates))
    

    def test_update_profile_used_template(self):
        """
        This tests check status code 
        and used template UpdateProfile
        """
        login = self.client.login(username='admin', password='abc564!')
        self.assertTrue(login)

        response = self.client.get(reverse('update_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'customactions/update_profile.html' in (t.name for t in response.templates))
        self.assertTrue(response, 'base.html' in (t.name for t in response.templates))
    

    def test_contact_used_template(self):
        """
        This tests check status code 
        and used template contact
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'customactions/contact.html' in (t.name for t in response.templates))
        self.assertTrue(response, 'base.html' in (t.name for t in response.templates))
        