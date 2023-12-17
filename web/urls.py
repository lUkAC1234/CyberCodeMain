from django.urls import path,include
from .views import index, about, contact, Pricing, pricinglist, \
BlogListView, blogdetail, job, JobDetailView, \
loginView, RegistrationView, MyProfileEdit, logoutView, FAQListView, \
payment_list, AddToCart, RemoveFromCart, SuccessPayment, PageNotFound, \
ProjectsView, ProjectDetailView, UserPasswordChangeView


app_name = "main"

urlpatterns = [
    # Main Page
    path('', index.as_view(), name="index"),

    # About us
    path('about/us/', about.as_view(), name="about"),

    # FAQ
    path('faq/list', FAQListView.as_view(), name="faqlist"),

    # Contact us
    path('contact/us/', contact.as_view(), name="contact"),

    # Pricing
    path('package/prices/', Pricing.as_view(), name="pricing"),
    path('payment/list', payment_list.as_view(), name="payment"),
    path('add_to_cart/<int:id>', AddToCart, name="add_to_cart"),
    path('remove_from_cart/<int:id>/', RemoveFromCart, name="removefromcart"),
    path('package/prices/list', pricinglist.as_view(), name="pricinglist"),
    path('success/checkout/', SuccessPayment.as_view(), name="thankyou"),

    # Blog
    path('website/blogs/list', BlogListView.as_view(), name="blog"),
    path('website/blog/detail/<int:pk>', blogdetail.as_view(), name="blogdetail"),

    # Job
    path('website/jobs/list/', job.as_view(), name="job"),
    path('website/job/detail/<int:pk>', JobDetailView.as_view(), name="jobdetail"),

    # Projects
    path('our/projects/list', ProjectsView.as_view(), name="projects"),
    path('project/detail/<int:pk>', ProjectDetailView.as_view(), name="projectdetail"),

    # User
    path('user/profile/', MyProfileEdit.as_view(), name="profile"),
    path('user/password/change', UserPasswordChangeView.as_view(), name="changeuserpassword"),
    path('login/', loginView, name="login"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('logout/account', logoutView, name="logout"),

    # Errors
    path('page/not/found/404/error', PageNotFound, name="page404"),

]
