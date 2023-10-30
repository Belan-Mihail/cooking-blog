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