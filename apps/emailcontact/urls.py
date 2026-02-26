from django.urls import path
from .views import success_view, contact_view

app = "emailcontact"

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("success/", success_view, name="success"),
]