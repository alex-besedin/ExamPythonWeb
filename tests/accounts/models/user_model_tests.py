# profile tests.py
import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from KetoGo.accounts.models import AppUser


class AppUserModelTests(TestCase):
    def test_user_create__when_valid__expect_correct_result(self):
        user = AppUser(
            email="test@user.com",
            password="Dfi!z.JA!4VRBeY",
            first_name='First-name',
            last_name='Last-name',
            avatar='https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            age=20,
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user.pk)

    def test_user_create__when_first_name_is_not_valid__expect_raise(self):
        user = AppUser(
            email="test@user.com",
            password="Dfi!z.JA!4VRBeY",
            first_name='First5',
            last_name='Last',
            avatar='https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            age=20,
        )

        with self.assertRaises(ValidationError) as error:
            user.full_clean()
            user.save()

        self.assertIsNotNone(error.exception)

    def test_user_create__when_last_name_is_not_valid__expect_raise(self):
        user = AppUser(
            email="test@user.com",
            password="Dfi!z.JA!4VRBeY",
            first_name='First',
            last_name='Last5',
            avatar='https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            age=20,
        )

        with self.assertRaises(ValidationError) as error:
            user.full_clean()
            user.save()

        self.assertIsNotNone(error.exception)

    def test_user_get_full_name__when_valid__expect_correct_result(self):
        user = AppUser(
            email="test@user.com",
            password="Dfi!z.JA!4VRBeY",
            first_name='First-name',
            last_name='Last-name',
            avatar='https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            age=20,
        )

        user.full_clean()
        user.save()
        expected_object_name = f'{user.first_name} {user.last_name}'

        self.assertEqual(user.get_full_name(), expected_object_name)

