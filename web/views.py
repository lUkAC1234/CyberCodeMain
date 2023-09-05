from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "pages/index.html"

class about(TemplateView):
    template_name = "pages/about.html"

class contact(TemplateView):
    template_name = "pages/contact.html"

class pricing(TemplateView):
    template_name = "pages/pricing.html"

class pricinglist(TemplateView):
    template_name = "pages/pricinglist.html"
    
class documentation(TemplateView):
    template_name = "pages/documentation.html"    

class blog(TemplateView):
    template_name = "pages/blog.html"    

class blogdetail(TemplateView):
    template_name = "pages/blogdetail.html"    

class job(TemplateView):
    template_name = "pages/job.html"    

class jobdetail(TemplateView):
    template_name = "pages/jobdetail.html"    

class helpcenter(TemplateView):
    template_name = "pages/helpcenter.html"    

class profile(TemplateView):
    template_name = "pages/profile.html"    

class login(TemplateView):
    template_name = "pages/login.html"    

class registration(TemplateView):
    template_name = "pages/registration.html"    