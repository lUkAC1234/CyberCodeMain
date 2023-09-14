from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import PostModel

class index(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = PostModel.objects.all()
        return data

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
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = PostModel.objects.all()
        data['latestPost'] = PostModel.objects.all().order_by('-id')[:1]
        return data  

class blogdetail(DetailView):
    model = PostModel
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