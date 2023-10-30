from django import forms

from .models import Profile

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