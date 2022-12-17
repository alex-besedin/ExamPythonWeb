from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core import validators
from KetoGo.core.validators import name_alphabetic_validator

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    first_name = forms.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First name...',
            },
        ),
        label="First Name",
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            name_alphabetic_validator,
        ),
    )
    last_name = forms.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last name...',
            },
        ),
        label="Last Name",
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            name_alphabetic_validator,
        ),
    )
    avatar = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'placeholder': 'Link to your photo...',
            },
        ),
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your age...',
            },
        ),
        validators=(
            validators.MinValueValidator(0, message="Age cannot be negative."),
        ),
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'avatar', 'age',)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        field_classes = {'username': auth_forms.UsernameField}
        fields = ('first_name', 'last_name', 'avatar', 'age',)  # the order should be as we want it to be seen
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'avatar': 'Link to Image',
            'age': 'Your Age',
        }
