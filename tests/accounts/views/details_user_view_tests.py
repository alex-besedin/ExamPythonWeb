from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy

from KetoGo.accounts.views import DetailsUserView
from KetoGo.common.models import ProductLike
from KetoGo.products.models import Product
from tests.common.base_test_case import BaseTestCase
from django.test import RequestFactory

UserModel = get_user_model()


class EditUserViewTests(BaseTestCase):
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
        user = UserModel.objects.create_user(**credentials, **appuser_data)

        # create and like 3 products:
        product_data1 = {
            'name': 'product1',
            'category': 'B',
            'product_photo': 'path_to_photo1',
            'description': 'some description',
            'price': 10,
        }
        # create product2:
        product1 = Product.objects.create(**product_data1)
        # like/add to favourites product1:
        ProductLike.objects.create(to_product=product1, to_user=user)

        product_data2 = {
            'name': 'product2',
            'category': 'C',
            'product_photo': 'path_to_photo2',
            'description': 'some description',
            'price': 10,
        }
        # create product2:
        product2 = Product.objects.create(**product_data2)
        # like/add to favourites product2:
        ProductLike.objects.create(to_product=product2, to_user=user)

        product_data3 = {
            'name': 'product3',
            'category': 'A',
            'product_photo': 'path_to_photo3',
            'description': 'some description',
            'price': 10,
        }
        # create product3:
        product3 = Product.objects.create(**product_data3)
        # like/add to favourites product3:
        ProductLike.objects.create(to_product=product3, to_user=user)

    def test_if_user_logs_in_upon_creation(self):
        user = UserModel.objects.get(id=1)
        user_is_logged_in = user.is_authenticated

        self.assertTrue(user_is_logged_in)

    # def test_details_user_view_context(self):
        # # GET response using RequestFactory().
        # factory = RequestFactory()
        # request = factory.get('/accounts/profile/1')
        # # request = factory.get(reverse('details user'), kwargs={'pk': 1})
        # # request = factory.get(reverse_lazy('details user'), kwargs={'pk': 1})
        # response = DetailsUserView.as_view()(request)

        # # GET response using the test client.
        # response = self.client.get('/accounts/profile/1')
        # response = self.client.get(reverse('details user', kwargs={'pk': 1}))
        # print(response.context)

        # # assert response.context['your_context']:
        # self.assertIsNone(response.context['is_owner'])
        # self.assertIsNone(response.context['full_name'])
        # self.assertIsNone(response.context['favourites'])
        # self.assertIn('is_owner', response.context)

        # sorted_favourites = ['A A named product3', 'A B named product1', 'A C named product2']

        # self.assertIsInstance(response.context_data, dict)
        # self.assertEqual(response.context_data['is_owner'], True)
        # self.assertEqual(response.context_data['full_name'], 'First Last')
        # self.assertEqual(response.context_data['favourites'], sorted_favourites)


