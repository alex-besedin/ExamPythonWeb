from django.contrib.auth import get_user_model
from django.db import models

from KetoGo.products.models import Product

UserModel = get_user_model()


# common models

class ProductComment(models.Model):
    # Product's field for all comments is named productcomment_set: {NAME_OF_THIS_MODEL.lower()}_set
    MAX_TEXT_LENGTH = 300

    class Meta:
        ordering = ['-date_and_time_of_publication', ]

    comment_text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        null=False,

    )
    to_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    to_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Comment for {self.to_product.name} by {self.to_user.get_full_name()}'


class ProductLike(models.Model):
    # Product's field for all likes is named productlike_set: {NAME_OF_THIS_MODEL.lower()}_set
    to_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    to_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'A like for {self.to_product.name} by {self.to_user.get_full_name()}'
