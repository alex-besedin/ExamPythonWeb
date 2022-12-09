from django.views import generic

from KetoGo.products.models import Product


class ProductsListView(generic.ListView):
    model = Product
    categories = ('salad', 'sandwich', 'chaffle', 'dessert')
    # categories = [x for x in dir(CategoryChoice) if x.isalpha()]
    template_name = 'products/menu.html'

    # paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = self.categories
        context['user'] = self.request.user

        return context


class AddProductView(generic.CreateView):
    pass


class EditProductView(generic.UpdateView):
    pass


class DeleteProductView(generic.DeleteView):
    pass


class DetailsProductView(generic.DetailView):
    model = Product
    template_name = 'products/details product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        #     #  this will make n+1 DB requests... not good!
        #     photos = self.object.photo_set.all()
        #     #  this will make 2 DB requests
        #     photos = self.object.photo_set.prefetch_related('photolike_set')
        #
        #     context['pets_count'] = self.object.pet_set.count()
        #     context['photos'] = self.object.photo_set.all()
        #     context['likes_count'] = sum(photo.photolike_set.count() for photo in photos)
        #     context['is_owner'] = self.request.user == self.object
        #     # self.object is the selected user by primary key(the owner of the profile viewed)
        #     # self.request.user is the logged user(the viewer that is browsing the profile)
        #     # context['photos_count'] = self.object.
        #
        return context

