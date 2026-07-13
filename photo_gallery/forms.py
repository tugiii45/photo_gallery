from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    """
    Handles user registration with username, email, and password.
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserLoginForm(AuthenticationForm):
    """
    Handles user authentication.
    """

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)