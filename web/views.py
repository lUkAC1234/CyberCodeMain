from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import PostModel, PricingModel, FeedbackModel, ContactusModel
from .forms import ContactusModelForm

class index(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pricing'] = PricingModel.objects.filter(popular=True).order_by('-popular', '-id')[:3]
        data['posts'] = PostModel.objects.all()
        data['feedbacks'] = FeedbackModel.objects.all()
        return data

class about(TemplateView):
    template_name = "pages/about.html"

class contact(CreateView):
    form_class = ContactusModelForm
    template_name = "pages/contact.html"
    success_url = '/contact/us/#contact-form' 
    success_message = "Your form has been submitted successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.successfully_submitted = True
        return super(contact, self).form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        self.success_url = self.success_url + '?error=true'
        return response

class pricing(TemplateView):
    template_name = "pages/pricing.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pricing'] = PricingModel.objects.filter(popular=True).order_by('-popular', '-id')[:3]
        return data

class pricinglist(ListView):
    model = PricingModel
    template_name = "pages/pricinglist.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        recommended_items = queryset.filter(recommended=True).order_by('-id')
        popular_items = queryset.filter(popular=True, recommended=False).order_by('-id')
        other_items = queryset.exclude(recommended=True, popular=True).order_by('-id')
        queryset = list(recommended_items) + list(popular_items) + list(other_items)
        
        # Deleting duplicate elements
        queryset = list({item.id: item for item in queryset}.values())

        return queryset

    
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