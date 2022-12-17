from KetoGo.common.models import ProductLike


def apply_likes_count(product):
    product.likes_count = product.productlike_set.count()
    return product


def apply_product_is_liked_or_not_by_user(product, logged_user):
    product.is_liked_by_user = None
    if ProductLike.objects.filter(to_product_id=product.pk, to_user_id=logged_user.pk).exists():
        product.is_liked_by_user = True
    else:
        product.is_liked_by_user = False
    return product


def sort_by_likes_count(list_of_product_objects):
    sorted_list = sorted(list_of_product_objects, key=lambda obj: obj.likes_count)
    return sorted_list
