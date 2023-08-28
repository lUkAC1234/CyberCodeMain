from django.urls import path
from .views import index, about, contact, pricing, pricinglist, \
documentation, blog, blogdetail, job, jobdetail

app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('about/us/', about.as_view(), name="about"),
    path('contact/us/', contact.as_view(), name="contact"),
    path('package/prices/', pricing.as_view(), name="pricing"),
    path('package/prices/list', pricinglist.as_view(), name="pricinglist"),
    path('website/documentation/', documentation.as_view(), name="documentation"),
    path('website/blogs/list', blog.as_view(), name="blog"),
    path('website/blog/detail/', blogdetail.as_view(), name="blogdetail"),
    path('website/jobs/list/', job.as_view(), name="job"),
    path('website/job/detail/', jobdetail.as_view(), name="jobdetail"),
]
