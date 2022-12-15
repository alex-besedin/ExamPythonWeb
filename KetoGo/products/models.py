from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from KetoGo.core.model_mixin import ChoicesEnumMixin


class CategoryChoice(ChoicesEnumMixin, Enum):
    salad = 'Salad'  # name is 'salad'(it will stay in DB), value is 'Salad' (it will visualise)
    sandwich = 'Sandwich'
    chaffle = 'Chaffle'
    dessert = 'Dessert'


class Product(models.Model):
    PRODUCT_NAME_MAX_LENGTH = 30
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
    )
    category = models.CharField(
        choices=CategoryChoice.choices(),
        max_length=CategoryChoice.max_len(),
    )
    product_photo = models.ImageField(
        upload_to='product_photos/',
    )
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return f'A {self.category} named {self.name}'
