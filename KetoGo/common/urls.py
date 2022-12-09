from django.urls import path

from KetoGo.common.views import index

urlpatterns = (
    path('', index, name='index'),
)