from django.urls import path

from KetoGo.common.views import like_product, comment_product, menu, index, search, EditCommentView, DeleteCommentView

urlpatterns = (
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('search/', search, name='search'),
    path('like/<int:product_id>/', like_product, name='like product'),
    path('comment/<int:product_id>/', comment_product, name='comment product'),
    path('comment/edit/<int:pk>/', EditCommentView.as_view(), name='edit comment'),
    path('comment/delete/<int:pk>/', DeleteCommentView.as_view(), name='delete comment'),
)
