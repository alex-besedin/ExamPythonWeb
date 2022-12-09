from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from KetoGo.accounts.managers import AppUserManager
from KetoGo.core.validators import name_alphabetic_validator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True)

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
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'avatar', 'age',)
    # creating a superuser from the terminal will require all fields.

    objects = AppUserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
