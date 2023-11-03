from django.test import TestCase
from customactions.models import Profile, Contact
from django.contrib.auth.models import User

class TestProfileModel(TestCase):
    """
    Test for Profile Model
    """
    def setUp(self):
        User.objects.create(username='admin',),
        self.profile = Profile.objects.create(
            nickname="administrator",
            bio='bio',
            user_id=1,
            region = "Germany",
            occupation='developper',
            )


    def test_profile_str(self):
        """
        Checks str for Profile Model
        """
        obj = self.profile
        self.assertEqual(str(obj), "admin")
    

    def test_checking_object_profile(self):
        """
        Check test model belongs profile Model 
        """
        obj = self.profile
        self.assertTrue(isinstance(obj, Profile))
    

    def test_profile_has_correctly_nickname(self):
        """
        Check profile nickname correctly
        """
        obj = self.profile
        self.assertEqual(obj.nickname, 'administrator')


class TestContactModel(TestCase):
    """
    Test for Contact Model
    """
    def setUp(self):
        self.contact = Contact.objects.create(
            name='mike',
            email='test@gmail.com',
            message='message',
            )


    def test_contact_str(self):
        """
        Checks str for Contact Model
        """
        obj = self.contact
        self.assertEqual(str(obj), "mike")
    

    def test_checking_object_contact(self):
        """
        Check test model belongs contact Model 
        """
        obj = self.contact
        self.assertTrue(isinstance(obj, Contact))
    

    def test_contact_has_correctly_message(self):
        """
        Check contact message correctly
        """
        obj = self.contact
        self.assertEqual(obj.message, 'message')
    