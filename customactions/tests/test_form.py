from django.test import TestCase
from customactions.forms import ProfileForm, ContactForm
from django.core.files.uploadedfile import SimpleUploadedFile
from customactions.models import Profile
from django.contrib.auth.models import User

class TestProfileForm(TestCase):
    """Test ProfileForm"""

    def test_profileform_fields(self):
        """
        test ProfileForm fields
        """
        form = ProfileForm()
        self.assertIn("nickname", form.fields)
        self.assertIn("avatar", form.fields)
        self.assertIn("bio", form.fields)
        self.assertIn("birth_date", form.fields)
        self.assertIn("region", form.fields)
        self.assertIn("occupation", form.fields)


    def test_profileform_with_valid_data(self):
        """test ProfileForm with valid data"""
        form = ProfileForm(data={
            'nickname': 'test nickname',
            'avatar': SimpleUploadedFile("image.jpg", b"file data"),
            'bio': 'test',
            'birth_date': '1988-08-14',
            'region': 'test-region',
            'occupation': 'test-occupation'

        })
        self.assertTrue(form.is_valid())
    

    def test_profileform_with_blank_fields_data(self):
        """
        test ProfileForm with blank data
        must return True since it is allowed by the model
        """
        form = ProfileForm(data={})
        self.assertTrue(form.is_valid())


    def test_profileform_with_invalid_data(self):
        """test ProfileForm with invalid data"""
        form = ProfileForm(data={
            'nickname': 'test nickname',
            'avatar': SimpleUploadedFile("image.jpg", b"file data"),
            'bio': 'test',
            # add invilid format of birth_date
            'birth_date': '14-08-1988',
            'region': 'test-region',
            'occupation': 'test-occupation'

        })
        self.assertFalse(form.is_valid())


    def test_profileform_invalid_format_of_birth_date(self):
        """test ProfileForm with invalid data"""
        form = ProfileForm(data={
            # add invilid format of birth_date
            'birth_date': '1988-08-41',
        })
        self.assertFalse(form.is_valid())
    

class TestContactForm(TestCase):
    """Test ContactForm"""

    def test_contactform_fields(self):
        """
        test ContactForm fields
        """

        form = ContactForm()
        self.assertIn("name", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("message", form.fields)
    

    def test_contactform_with_valid_data(self):
        """test ContactForm with valid data"""
        form = ContactForm(data={
            'name': 'test name',
            'email': 'test@mail.gcom',
            'message': 'test message',
        })
        self.assertTrue(form.is_valid())
    

    def test_contactform_with_invalid_data(self):
        """test ContactForm with invalid data"""
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
    

    def test_contactform_name_more_then_max_length(self):
        """test ContactForm with name length 121 symbol"""
        form = ContactForm(data={
            'name': 't'*121,
            'email': 'test@mail.gcom',
            'message': 'test message',
        })
        self.assertFalse(form.is_valid())
    

    def test_contactform_message_more_then_max_length(self):
        """test ContactForm with name length 121 symbol"""
        form = ContactForm(data={
            'name': 't',
            'email': 'test@mail.gcom',
            'message': 't'*1001,
        })
        self.assertFalse(form.is_valid())