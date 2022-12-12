from django import forms

from KetoGo.products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'product_photo', 'description')  # the order should be as we want it to be seen
        labels = {
            'name': 'Product Name',
            'category': 'Category',
            'product_photo': 'Link to Image',
            'description': 'Description',
        }


class ProductCreateForm(ProductBaseForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)


class ProductEditForm(ProductBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProductDeleteForm(ProductBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # super(PetCreateForm, self).__init__(*args, **kwargs)

        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
