from django.contrib.auth import views as auth_views, login, get_user_model, mixins
from django.urls import reverse_lazy
from django.views import generic

from KetoGo.accounts.forms import RegisterUserForm
from KetoGo.core.product_utils import apply_product_is_liked_or_not_by_user
from KetoGo.products.models import Product

UserModel = get_user_model()


class RegisterUserView(generic.CreateView):
    template_name = 'auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    # after registration automatically logs the user in:
    def form_valid(self, form):
        result = super().form_valid(form)
        # if the form is ok and is sent to DB, log in the user with given credentials
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'auth/login.html'


class LogoutUserView(auth_views.LogoutView):
    template_name = 'auth/logout.html'


class DetailsUserView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = [apply_product_is_liked_or_not_by_user(product, self.object) for product in Product.objects.all()]
        favourites = [product for product in products if product.is_liked_by_user]

        context['is_owner'] = self.request.user == self.object
        #     # self.object is the selected user by primary key(the owner of the profile viewed)
        #     # self.request.user is the logged user(the viewer that is browsing the profile)
        context['full_name'] = self.object.get_full_name()
        context['favourites'] = favourites
        return context


class EditUserView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    # form_class = EditUserForm
    fields = ('first_name', 'last_name', 'avatar', 'age',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.object.pk})
        # return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})


class DeleteUserView(mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

