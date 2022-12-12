from django.contrib.auth import mixins, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from KetoGo.common.forms import SearchProductForm, ProductCommentForm
from KetoGo.common.models import ProductLike
from KetoGo.core.product_utils import apply_likes_count, apply_product_is_liked_or_not_by_user
from KetoGo.products.models import Product
from django.db.models import Q

UserModel = get_user_model()


def index(request):
    return render(request, 'common/home-page.html')


def menu(request):
    search_form = SearchProductForm()
    products = Product.objects.all()

    context = {
        'search_form': search_form,
        'products': products,
        'categories': [
            'salad',
            'sandwich',
            'chaffle',
            'dessert',
        ],
    }

    return render(request, 'common/menu.html', context)


def search(request):
    search_results = []
    search_string = None

    if request.method == "GET":
        search_string = request.GET.get('search')

        if search_string == '':
            search_string = 'None'
        else:
            # Use & (AND) operator to search for more than 2 fields.
            # Use | (OR) operator to search for only one field.
            search_results = Product.objects.all().filter(
                Q(category__icontains=search_string) |
                Q(description__icontains=search_string) |
                Q(name__icontains=search_string)
            )

    search_results = [apply_likes_count(search_result) for search_result in search_results]

    context = {
        'products': search_results,
        'search_string': search_string,
        'products_count': len(search_results),
    }
    return render(request, 'common/search.html', context)


@login_required
def like_product(request, product_id):
    product_is_liked_by_user = ProductLike.objects.filter(
        to_product_id=product_id,
        to_user_id=request.user.pk
    )

    if product_is_liked_by_user:
        product_is_liked_by_user.delete()

    else:
        ProductLike.objects.create(
            to_product_id=product_id,
            to_user_id=request.user.pk,
        )

    redirect_path = request.META['HTTP_REFERER']

    return redirect(redirect_path)


@login_required
def comment_product(request, product_id):
    product = Product.objects.filter(pk=product_id).get()

    form = ProductCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # Does not save to DB yet
        comment.to_product = product
        comment.to_user = request.user
        comment.save()

    return redirect('details product', pk=product_id)
