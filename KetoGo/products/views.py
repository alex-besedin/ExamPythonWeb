from django.contrib.auth import mixins

from django.urls import reverse_lazy
from django.views import generic

from KetoGo.common.forms import ProductCommentForm
from KetoGo.core.product_utils import apply_likes_count, apply_product_is_liked_or_not_by_user
from KetoGo.products.forms import CreateProductForm, EditProductForm
from KetoGo.products.models import Product


class AddProductView(mixins.LoginRequiredMixin, generic.CreateView):
    template_name = 'products/add product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('menu')


class EditProductView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'products/edit product.html'
    form_class = EditProductForm

    def get_success_url(self):
        return reverse_lazy('details product', kwargs={'pk': self.object.pk})


class DeleteProductView(mixins.LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'products/delete product.html'
    success_url = reverse_lazy('menu')


class DetailsProductView(generic.DetailView):
    model = Product
    template_name = 'products/details product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comment_form = ProductCommentForm()
        product = self.object
        user = self.request.user

        apply_likes_count(product)
        apply_product_is_liked_or_not_by_user(product, user)
        comments_for_product = product.productcomment_set.all()

        context['comments'] = comments_for_product
        context['comment_form'] = comment_form

        return context
