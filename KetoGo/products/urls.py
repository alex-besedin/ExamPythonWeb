from django.urls import path, include

from KetoGo.products.views import AddProductView, DetailsProductView, EditProductView, DeleteProductView

urlpatterns = (
    path('add/', AddProductView.as_view(), name='add product'),
    path('<int:pk>/', include([
        path('', DetailsProductView.as_view(), name='details product'),
        path('edit/', EditProductView.as_view(), name='edit product'),
        path('delete/', DeleteProductView.as_view(), name='delete product'),
    ])),
)
