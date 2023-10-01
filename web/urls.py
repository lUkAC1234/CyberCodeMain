from django.urls import path,include
from .views import index, about, contact, Pricing, pricinglist, \
documentation, BlogListView, blogdetail, job, JobDetailView, helpcenter, \
loginView, RegistrationView, MyProfileEdit, logoutView, FAQListView, \
PaymentListView

app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('about/us/', about.as_view(), name="about"),
    path('contact/us/', contact.as_view(), name="contact"),
    path('package/prices/', Pricing.as_view(), name="pricing"),
    path('package/prices/list', pricinglist.as_view(), name="pricinglist"),
    path('payment/list', PaymentListView.as_view(), name="payment"),
    path('website/documentation/', documentation.as_view(), name="documentation"),
    path('website/blogs/list', BlogListView.as_view(), name="blog"),
    path('website/blog/detail/<int:pk>', blogdetail.as_view(), name="blogdetail"),
    path('website/jobs/list/', job.as_view(), name="job"),
    path('website/job/detail/<int:pk>', JobDetailView.as_view(), name="jobdetail"),
    path('help/center/', helpcenter.as_view(), name="helpcenter"),
    path('user/profile/', MyProfileEdit.as_view(), name="profile"),
    path('login/', loginView, name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('logout/account', logoutView, name="logout"),
    path('faq/list', FAQListView.as_view(), name="faqlist"),

]
