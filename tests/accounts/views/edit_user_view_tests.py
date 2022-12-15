from django.contrib.auth import get_user_model

from tests.common.base_test_case import BaseTestCase

UserModel = get_user_model()


class EditUserViewTests(BaseTestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        appuser_data = {
            'email': 'some@email.com',
            'password': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }

        UserModel.objects.create(**appuser_data)

    def test_edit_user_view_get_absolute_url(self):
        user = UserModel.objects.get(id=1)
        # on success expect to show user details page:
        expected_url = '/accounts/profile/1/'
        # This will also fail if the urlconf is not defined.
        self.assertEqual(user.get_absolute_url(), expected_url)
