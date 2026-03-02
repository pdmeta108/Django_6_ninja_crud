from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Include the URLs from person app.
    path('', include('apps.person.urls')),

    # Include the URLs from product app.
    path('products/', include('apps.product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)