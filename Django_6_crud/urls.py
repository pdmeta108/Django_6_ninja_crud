from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI, Redoc
from apps.person.api import router as persons_router

api = NinjaAPI(docs=Redoc())
api.add_router("/persons", persons_router)


urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Include the URLs from person app.
    path('', include('apps.person.urls')),

    # Include the URLs from product app.
    path('products/', include('apps.product.urls')),

    # API route
    path('api/', api.urls)
]
