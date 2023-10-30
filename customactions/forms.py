from django import forms

from .models import Profile, Contact

class ProfileForm(forms.ModelForm):
    """
    A form class for the profile models
    """

    class Meta:
        model = Profile
        fields = ['nickname', 'avatar', 'bio', 'birth_date', 'region', 'occupation']

        widgets = {
            'nickname': forms.TextInput(
                attrs={
                    'placeholder': 'Your nickname'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'placeholder': 'A few words about yourself'
                }
            ),
            'birth_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'placeholder': 'year-month-date (1988-08-14)'
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'placeholder': 'Your region'
                }
            ),
            'occupation': forms.TextInput(
                attrs={
                    'placeholder': 'Your occupation'
                }
            )
        }


class ContactForm(forms.ModelForm):
    """
    A form class for the contact models
    """
    class Meta:
        model = Contact

        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Your email for answer'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Your message'
                }
            )
        }