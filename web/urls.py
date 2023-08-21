from django.urls import path
from .views import index, about, contact, pricing

app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('about/us/', about.as_view(), name="about"),
    path('contact/us/', contact.as_view(), name="contact"),
    path('package/prices/', pricing.as_view(), name="pricing"),
]
