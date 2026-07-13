from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


INPUT_CLASSES = (
    "w-full px-4 py-3 border border-gray-300 rounded-lg "
    "focus:outline-none focus:ring-2 focus:ring-gray-900"
)


class UserRegistrationForm(UserCreationForm):
    """
    Handles user registration with username, email, and password.
    """

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": INPUT_CLASSES}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": INPUT_CLASSES}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs["class"] = INPUT_CLASSES
        self.fields["password2"].widget.attrs["class"] = INPUT_CLASSES


class UserLoginForm(AuthenticationForm):
    """
    Handles user authentication.
    """

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": INPUT_CLASSES}
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": INPUT_CLASSES}
        ),
    )