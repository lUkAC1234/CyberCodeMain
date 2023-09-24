from typing import Any
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import PostModel, PricingModel, FeedbackModel, ContactusModel, FaqModel, JobModel, \
PostCategoryModel, PostTagModel, UserModel
from .forms import ContactusModelForm, AccountForm, LoginForm, RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

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
    success_url = '/contact/us/' 

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['faqs'] = FaqModel.objects.all()[:8]
        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            form.save()
            response_data = {'success': True}
            if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse(response_data)
        except Exception as e:
            errors = {field: [error for error in form[field].errors] for field in form.fields}
            if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': errors})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = {field: [error for error in form[field].errors] for field in form.fields}
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': errors})
        return super().form_invalid(form)

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

class BlogListView(ListView):
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

class MyProfileEdit(UpdateView):
    model = UserModel
    form_class = AccountForm 
    template_name = "pages/profile.html"
    success_url = reverse_lazy('main:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
def loginView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('main:login')
    else:
        template_name = 'pages/login.html'
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return JsonResponse({'success': True, 'redirect': reverse('main:index')})
                form.add_error('password', f'Username or password is incorrect')

            errors = {field: [error for error in form[field].errors] for field in form.fields}
            return JsonResponse({'success': False, 'errors': errors})

        return render(request, template_name, {'form': LoginForm()})

    
class RegistrationView(CreateView):
    model = UserModel
    form_class = RegistrationForm
    template_name = 'pages/registration.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password'])
        del form.cleaned_data['confirm_password']

        response = super().form_valid(form)
        login(self.request, self.object) 
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        errors = {field: [error for error in form[field].errors] for field in form.fields}
        return JsonResponse({'success': False, 'errors': errors})
    
def logoutView(request):
    logout(request)
    return redirect('main:index')