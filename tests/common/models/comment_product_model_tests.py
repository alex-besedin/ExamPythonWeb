import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase

from KetoGo.common.models import ProductComment
from KetoGo.products.models import Product

UserModel = get_user_model()


class TestCommentProductModels(TestCase):
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
        # create user
        UserModel.objects.create_user(**credentials, **appuser_data)

        # create a product:
        product_data1 = {
            'name': 'product1',
            'category': 'B',
            'product_photo': 'path_to_photo1',
            'description': 'some description',
            'price': 10,
        }
        # create product2:
        Product.objects.create(**product_data1)

    def test_str_of_CommentProduct_object__expect_correct(self):
        product1 = Product.objects.get(id=1)
        user = UserModel.objects.get(id=1)

        comment_data = {
            'comment_text': 'test comment',
            'date_and_time_of_publication': '2022-12-14 12:32:51.197853 +00:00',
            'to_product': product1,
            'to_user': user,
        }
        comment = ProductComment.objects.create(**comment_data)

        expected_str = 'A comment for product1 by First Last'

        self.assertEqual(comment.__str__(), expected_str)

