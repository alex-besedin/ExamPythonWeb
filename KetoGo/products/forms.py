from django import forms

from KetoGo.products.models import Product


class BaseProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'product_photo', 'description')  # the order should be as we want it to be seen
        #  "currently" field does not look ok in our form,so we change the Input type:
        widgets = {
            'product_photo': forms.FileInput(),
        }
        labels = {
            'name': 'Product Name',
            'category': 'Category',
            'price': 'Product Price',
            'product_photo': 'Upload Image',
            'description': 'Description',
        }


class CreateProductForm(BaseProductForm):
    pass


class EditProductForm(BaseProductForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
