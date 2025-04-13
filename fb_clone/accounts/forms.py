from django import forms
from .models import UserCredential

class CredentialForm(forms.ModelForm):
    class Meta:
        model = UserCredential
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Email or phone'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
        }
