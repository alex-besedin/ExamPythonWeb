from django.test import TestCase

from KetoGo.accounts.forms import RegisterUserForm


class RegisterUserFormsTests(TestCase):
    def test_register_user_form__when_valid__expect_form_is_valid(self):
        appuser_data = {
            'email': 'some@email.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
            'first_name': 'First-name',
            'last_name': 'Last-name',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        form = RegisterUserForm(appuser_data)
        # print(form)

        self.assertTrue(form.is_valid())


    def test_register_user_form__when_first_name_not_alfa_or_hyphen__expect_form_not_valid(self):
        appuser_data = {
            'email': 'some@email.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
            'first_name': 'First-5555',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        form = RegisterUserForm(appuser_data)

        self.assertFalse(form.is_valid())

    def test_register_user_form__when_last_name_not_alfa_or_hyphen__expect_form_not_valid(self):
        appuser_data = {
            'email': 'some@email.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last-5555',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': 20,
        }
        form = RegisterUserForm(appuser_data)

        self.assertFalse(form.is_valid())

    def test_register_user_form__when_age_is_negative__expect_form_not_valid(self):
        appuser_data = {
            'email': 'some@email.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last',
            'avatar': 'https://static01.nyt.com/images/2013/12/02/arts/arts2/arts2-superJumbo.jpg',
            'age': -1,
        }
        form = RegisterUserForm(appuser_data)

        self.assertFalse(form.is_valid())
