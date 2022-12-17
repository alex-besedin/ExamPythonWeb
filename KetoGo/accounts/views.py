from django.contrib.auth import views as auth_views, login, get_user_model, mixins
from django.urls import reverse_lazy
from django.views import generic

from KetoGo.accounts.forms import RegisterUserForm, EditUserForm
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
    template_name = 'accounts/details profile.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        products = [apply_product_is_liked_or_not_by_user(product, self.object) for product in Product.objects.all()]
        favourites = [product for product in products if product.is_liked_by_user]
        sorted_favourites = sorted(favourites, key=lambda obj: obj.category)

        context['is_owner'] = self.request.user == self.object
        #     # self.object is the selected user by primary key(the owner of the profile viewed)
        #     # self.request.user is the logged user(the viewer that is browsing the profile)
        context['full_name'] = self.object.get_full_name()
        context['favourites'] = sorted_favourites
        return context


class EditUserView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/edit profile.html'
    model = UserModel
    form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.object.pk})
        # return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})


class DeleteUserView(mixins.LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/delete profile.html'
    model = UserModel
    success_url = reverse_lazy('index')

