from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from KetoGo import settings
from KetoGo.core.exception_handler import my500_custom_error_view, my404_custom_page_not_found_view, \
    my400_custom_bad_request_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('KetoGo.common.urls')),
    path('accounts/', include('KetoGo.accounts.urls')),
    path('products/', include('KetoGo.products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = my500_custom_error_view
handler404 = my404_custom_page_not_found_view
handler400 = my400_custom_bad_request_view




# if settings.DEBUG:
#     urlpatterns += (
#         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     )
