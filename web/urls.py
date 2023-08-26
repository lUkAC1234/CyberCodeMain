from django.urls import path
from .views import index, about, contact, pricing, pricinglist, \
documentation, blog

app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('about/us/', about.as_view(), name="about"),
    path('contact/us/', contact.as_view(), name="contact"),
    path('package/prices/', pricing.as_view(), name="pricing"),
    path('package/prices/list', pricinglist.as_view(), name="pricinglist"),
    path('website/documentation/', documentation.as_view(), name="documentation"),
    path('website/blogs/list', blog.as_view(), name="blog"),
]
