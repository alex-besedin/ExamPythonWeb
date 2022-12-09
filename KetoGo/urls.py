from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from KetoGo import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('KetoGo.common.urls')),
    path('accounts/', include('KetoGo.accounts.urls')),
    path('products/', include('KetoGo.products.urls')),

]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
