from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from KetoGo.accounts.managers import AppUserManager
from KetoGo.core.validators import name_alphabetic_validator


class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    email = models.EmailField(
        unique=True,
    )
    date_joined = models.DateField(
        auto_now_add=True,
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            name_alphabetic_validator,
        )
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            name_alphabetic_validator,
        )
    )
    avatar = models.URLField(
        null=False,
        blank=True,
    )
    age = models.PositiveIntegerField()

    # user credentials consist of 'email' and 'password'

    REQUIRED_FIELDS = ('first_name', 'last_name', 'avatar', 'age',)
    USERNAME_FIELD = 'email'

    objects = AppUserManager()
