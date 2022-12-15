from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


class RegisterUserViewTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        credentials = {
            'email': 'some@email.com',
            'password': 'somepassword',
        }
        appuser_data = {
            # 'email': 'some@email.com',
            # 'password': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        UserModel.objects.create_user(**credentials, **appuser_data)

    def test_create_user_view__when_correct__expect_to_create_user(self):
        appuser_data = {
            # 'email': 'some@email.com',
            # 'password': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        #   see if we have a user
        response = self.client.post(
            reverse('register user'),
            data=appuser_data,
        )

        created_user = UserModel.objects.filter(**appuser_data).get()

        self.assertIsNotNone(created_user)
        self.assertEqual(200, response.status_code)

    def test_user_with_same_credentials_is_logged__when_create_profile__expect_user_logged(self):
        credentials = {
            'email': 'some@email.com',
            'password': 'somepassword',
        }

        # check if a user is logged with given credentials
        self.assertTrue(self.client.login(**credentials))

    def test_if_user_logs_in_upon_creation(self):
        user = UserModel.objects.get(id=1)
        user_is_logged_in = user.is_authenticated

        self.assertTrue(user_is_logged_in)
