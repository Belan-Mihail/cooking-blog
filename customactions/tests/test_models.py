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
    

   