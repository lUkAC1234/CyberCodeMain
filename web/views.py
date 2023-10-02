from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView
from .models import PostModel, PricingModel, FeedbackModel, ContactusModel, FaqModel, JobModel, \
PostCategoryModel, PostTagModel, UserModel, PartnersModel, JobApplyModel, CheckOut
from .forms import ContactusModelForm, AccountForm, LoginForm, RegistrationForm, JobApplyForm, \
CheckOutForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin

class index(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pricing'] = PricingModel.objects.filter(popular=True).order_by('-popular', '-id')[:3]
        data['posts'] = PostModel.objects.all()
        data['feedbacks'] = FeedbackModel.objects.all()
        data['partners'] = PartnersModel.objects.all()
        return data

class about(TemplateView):
    template_name = "pages/about.html"

class contact(CreateView):
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
    
class FAQListView(ListView):
    model = FaqModel
    template_name = "pages/faqlist.html"

class Pricing(TemplateView):
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
        
        queryset = list({item.id: item for item in queryset}.values())

        return queryset

def AddToCart(request, id):
    cart = request.session.get('cart', [])

    if not cart:
        request.session['cart'] = []
        cart = request.session.get('cart', [])
    if id not in cart:
        cart.append(id)

    request.session['cart'] = cart

    return redirect('main:payment')

def RemoveFromCart(request, id):
    cart = request.session.get('cart', [])
    if id in cart:
        cart.remove(id)
        request.session['cart'] = cart
    return redirect('main:payment')

class payment_list(CreateView):
    template_name = 'pages/paymentlist.html'
    form_class = CheckOutForm

    def get_success_url(self):
        return reverse('main:thankyou')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])
        data['cart_items'] = PricingModel.get_cart_objects(cart)
        return data

    def form_valid(self, form):
        cart = self.request.session.get('cart', [])
        queryset = PricingModel.get_cart_objects(cart)
        total_price = sum(item.price for item in queryset)
        form.instance.total_price = total_price
        form.instance.user = self.request.user
        data = form.save()
        data.item.set(queryset)
        self.request.session['cart'] = []
        return super(payment_list, self).form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    
class SuccessPayment(TemplateView):
    template_name = "pages/thankyou.html"

    
class documentation(TemplateView):
    template_name = "pages/documentation.html"    

class BlogListView(ListView):
    template_name = "pages/blog.html"
    model = PostModel

    def get_queryset(self):
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

    def render_to_response(self, context, **response_kwargs):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            html = render_to_string('pages/blog_result.html', {'object_list': context['object_list']}, request=self.request)
            return JsonResponse({'success': True, 'html': html})
        return super().render_to_response(context, **response_kwargs)


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

class JobDetailView(DetailView):
    model = JobModel
    template_name = "pages/jobdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_job = self.object
        context['other_jobs'] = JobModel.objects.filter(category=current_job.category).exclude(pk=current_job.pk)[:3]
        context['apply_form'] = JobApplyForm(initial={'category': current_job.category})
        return context

    def post(self, request, pk):
        current_job = self.get_object()
        form = JobApplyForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.instance.category = current_job.category
            form.save()
            response_data = {'success': True}
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse(response_data) 
            return redirect('main:jobdetail', pk=current_job.pk)
        
        errors = {field: [error for error in form[field].errors] for field in form.fields}
        response_data = {'success': False, 'errors': errors}
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse(response_data)
        
        context = self.get_context_data(object=current_job)
        context['apply_form'] = form
        return self.render_to_response(context)

class helpcenter(TemplateView):
    template_name = "pages/helpcenter.html"       

class MyProfileEdit(LoginRequiredMixin, UpdateView):
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

        return render(request, template_name, {
            'form': LoginForm(),
            'googleLoginUrl': '/accounts/login/',
        })

    
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