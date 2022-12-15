from django.test import TestCase
from KetoGo.products.models import Product


class TestLikeProductModels(TestCase):
    def test_str_of_Product_object__expect_correct(self):
        product_data = {
            'name': 'keto sandwich',
            'category': 'sandwich',
            'product_photo': 'path_to_photo1',
            'description': 'some description',
            'price': 10,
        }
        # create product:
        product = Product.objects.create(**product_data)

        expected_str = 'A sandwich named keto sandwich'

        self.assertEqual(product.__str__(), expected_str)
