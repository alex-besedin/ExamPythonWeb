from django.contrib.auth import get_user_model
from django.test import TestCase
from KetoGo.accounts.models import AppUser
UserModel = get_user_model()


class BaseTestCase(TestCase):
    def create_and_login_user(self, email, password, **extra_fields):
        # create user
        user = UserModel.objects.create_user(email, password, **extra_fields)
        # login that user
        credentials = {
            'email': email,
            'password': password,
        }
        self.client.login(**credentials)
        return user

    def create_user(self, email, password, **extra_fields):
        # create user
        user = UserModel.objects.create_user(email, password, **extra_fields)
        return user
