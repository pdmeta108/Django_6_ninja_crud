from django.contrib import admin
from django.urls import include, path
from .api import api


urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Include the URLs from person app.
    path('', include('apps.person.urls')),

    # Include the URLs from product app.
    path('products/', include('apps.product.urls')),

    # API route
    path("api/", api.urls),
]
