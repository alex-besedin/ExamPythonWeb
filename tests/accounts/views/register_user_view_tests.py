from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


class RegisterUserViewTests(BaseTestCase):
    def test_create_user_view__when_correct__expect_to_create_profile(self):
        appuser_data = {
            'first_name': 'First',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        # make credentials
        credentials = {
            'email': 'some@email.com',
            'password': 'somepassword',
        }
        self.create_user(**credentials, **appuser_data)

        #   see if we have a user
        response = self.client.post(
            reverse('register user'),
            data=appuser_data,
        )

        created_user = UserModel.objects.filter(**appuser_data).get()

        self.assertIsNotNone(created_user)
        self.assertEqual(200, response.status_code)

    def test_user_is_logged_in__when_create_profile__expect_user_logged(self):
        credentials = {
            'email': 'some@email.com',
            'password': 'somepassword',
        }

        appuser_data = {
            'first_name': 'First',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        # create user
        UserModel.objects.create_user(**credentials, **appuser_data)

        # check if that user is logged in after creation
        self.assertTrue(self.client.login(**credentials))
