from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from KetoGo.core.model_mixin import StrFromFieldMixin, ChoicesEnumMixin


class CategoryChoice(ChoicesEnumMixin, Enum):
    salad = 'Salad'  # name is 'salad'(it will stay in DB), value is 'Salad' (it will visualise)
    sandwich = 'Sandwich'
    chaffle = 'Chaffle'
    dessert = 'Dessert'


class Product(StrFromFieldMixin, models.Model):
    PRODUCT_NAME_MAX_LENGTH = 30
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    str_fields = ('id', 'name',)

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
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:  # dynamically create unique slug
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

