from typing import Any
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import PostModel, PricingModel, FeedbackModel, ContactusModel, FaqModel, JobModel, \
PostCategoryModel, PostTagModel 
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

class contact(SuccessMessageMixin, CreateView):
    form_class = ContactusModelForm
    template_name = "pages/contact.html"
    success_url = '/contact/us/#contact-form' 
    success_message = "Your form has been submitted successfully."

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['faqs'] = FaqModel.objects.all()[:8]
        return data

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

class blog(ListView):
    template_name = "pages/blog.html"    
    def get_queryset(self):
        posts = PostModel.objects.all()
        search = self.request.GET.get('search', '')
        tag = self.request.GET.get("tag", '')
        category = self.request.GET.get("category", '')

        posts = PostModel.objects.all()

        if search: 
            posts = posts.filter(title__icontains=search)

        if tag and tag.isdigit():
            if PostTagModel.objects.filter(id=tag).exists():
                posts = posts.filter(tags=tag)
            else:
                posts = PostModel.objects.none()

        if category and category.isdigit():
            if PostCategoryModel.objects.filter(id=category).exists():
                posts = posts.filter(category=category)
            else:
                posts = PostModel.objects.none()

        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latestPost'] = PostModel.objects.all().order_by('-id')[:1]
        context['postCategories'] = PostCategoryModel.objects.all()
        context['postTags'] = PostTagModel.objects.all()
        return context

class blogdetail(DetailView):
    model = PostModel
    template_name = "pages/blogdetail.html"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.get_object()

        similar_posts = PostModel.objects.filter(
            Q(category=current_post.category) | Q(tags__in=current_post.tags.all())
        ).exclude(id=current_post.id)[:2]

        context['similarPosts'] = similar_posts
        return context 

class job(ListView):
    model = JobModel
    template_name = "pages/job.html"    

class jobdetail(DetailView):
    model = JobModel
    template_name = "pages/jobdetail.html"   

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        current_job = self.get_object()
        data['other_jobs'] = JobModel.objects.filter(category=current_job.category).exclude(id=current_job.id)[:3]
        return data  

class helpcenter(TemplateView):
    template_name = "pages/helpcenter.html"    

class profile(TemplateView):
    template_name = "pages/profile.html"    

class login(TemplateView):
    template_name = "pages/login.html"    

class registration(TemplateView):
    template_name = "pages/registration.html"    