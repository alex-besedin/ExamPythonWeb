from django.test import TestCase

from KetoGo.products.forms import CreateProductForm, EditProductForm


# BaseProductForm is the parent form
class ProductFormsTests(TestCase):
    def test_create_product_form__has_the_fields(self):
        form = CreateProductForm()
        self.assertIn("name", form.fields)
        self.assertIn("category", form.fields)
        self.assertIn("price", form.fields)
        self.assertIn("product_photo", form.fields)
        self.assertIn("description", form.fields)

    def test_create_product_form__name_field_label(self):
        form = CreateProductForm()
        name_label = form.fields['name'].label
        expected_name_label = 'Product Name'

        self.assertEqual(name_label, expected_name_label)

    def test_create_product_form__category_field_label(self):
        form = CreateProductForm()
        category_label = form.fields['category'].label
        expected_category_label = 'Category'

        self.assertEqual(category_label, expected_category_label)

    def test_create_product_form__price_field_label(self):
        form = CreateProductForm()
        price_label = form.fields['price'].label
        expected_price_label = 'Product Price'

        self.assertEqual(price_label, expected_price_label)

    def test_create_product_form__product_photo_field_label(self):
        form = CreateProductForm()
        product_photo_label = form.fields['product_photo'].label
        expected_product_photo_label = 'Upload Image'

        self.assertEqual(product_photo_label, expected_product_photo_label)

    def test_create_product_form__description_field_label(self):
        form = CreateProductForm()
        description_label = form.fields['description'].label
        expected_description_label = 'Description'

        self.assertEqual(description_label, expected_description_label)

    def test_edit_product_form__has_the_fields(self):
        form = EditProductForm()
        self.assertIn("name", form.fields)
        self.assertIn("category", form.fields)
        self.assertIn("price", form.fields)
        self.assertIn("product_photo", form.fields)
        self.assertIn("description", form.fields)

    def test_edit_product_form__name_field_label(self):
        form = EditProductForm()
        name_label = form.fields['name'].label
        expected_name_label = 'Product Name'

        self.assertEqual(name_label, expected_name_label)

    def test_edit_product_form__category_field_label(self):
        form = EditProductForm()
        category_label = form.fields['category'].label
        expected_category_label = 'Category'

        self.assertEqual(category_label, expected_category_label)

    def test_edit_product_form__price_field_label(self):
        form = EditProductForm()
        price_label = form.fields['price'].label
        expected_price_label = 'Product Price'

        self.assertEqual(price_label, expected_price_label)

    def test_edit_product_form__product_photo_field_label(self):
        form = EditProductForm()
        product_photo_label = form.fields['product_photo'].label
        expected_product_photo_label = 'Upload Image'

        self.assertEqual(product_photo_label, expected_product_photo_label)

    def test_edit_product_form__description_field_label(self):
        form = EditProductForm()
        description_label = form.fields['description'].label
        expected_description_label = 'Description'

        self.assertEqual(description_label, expected_description_label)


