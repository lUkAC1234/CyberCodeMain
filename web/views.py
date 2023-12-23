from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import PostModel, PricingModel, FeedbackModel, FaqModel, JobModel, \
PostCategoryModel, PostTagModel, UserModel, PartnersModel, CheckOut, ProjectModel, ProjectCategory
from .forms import ContactusModelForm, AccountForm, LoginForm, RegistrationForm, JobApplyForm, \
CheckOutForm, FeedbackForm, UserPasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.db.models import Count
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.utils import timezone

class index(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pricing'] = PricingModel.objects.filter(popular=True).order_by('-popular', '-id')[:3]
        data['posts'] = PostModel.objects.only('title', 'image', 'posted_on', 'short_description').all()
        data['feedbacks'] = FeedbackModel.objects.select_related('user').filter(is_allowed=True)
        data['partners'] = PartnersModel.objects.all()
        return data
    
class about(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['users'] = CheckOut.objects.only('user').all()
        return data

class contact(CreateView):
    form_class = ContactusModelForm
    template_name = "pages/contact.html"
    success_url = '/contact/us/' 

    def get_context_data(self, **kwargs):
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
    template_name = "pages/pricing/pricing.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pricing'] = PricingModel.objects.filter(popular=True).order_by('-popular', '-id')[:3]
        return data
    
class pricinglist(ListView):
    model = PricingModel
    template_name = "pages/pricing/pricinglist.html"
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
    template_name = 'pages/pricing/paymentlist.html'
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
        form.instance.total_price = sum(item.price for item in queryset)
        form.instance.user = self.request.user
        form.instance.success_checkout = 1
        data = form.save()
        data.item.set(queryset)
        self.request.session['cart'] = []
        self.request.session['success_checkout'] = True
        return super(payment_list, self).form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class SuccessPayment(CreateView):
    form_class = FeedbackForm
    template_name = "pages/pricing/thankyou.html"

    def get_success_url(self):
        return reverse('main:pricing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main:page404')
        
        if self.request.session.get('success_checkout', False):
            self.request.session['success_checkout'] = False
            return super().get(request, *args, **kwargs)
        
        return redirect('main:page404')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        CheckOut.objects.filter(user=self.request.user, success_checkout=True).update(success_checkout=True)
        return data  

class BlogListView(ListView):
    template_name = "pages/blog/blog.html"
    paginate_by = 5
    model = PostModel

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        tag = self.request.GET.get("tag", '')
        category = self.request.GET.get("category", '')

        posts = PostModel.objects.all().select_related('category')
 
        if search:
            posts = posts.filter(title__icontains=search)

        if tag and tag.isdigit():
            if PostTagModel.objects.filter(id=tag).exists():
                posts = posts.filter(tags=tag)

        if category and category.isdigit():
            if PostCategoryModel.objects.filter(id=category).exists():
                posts = posts.filter(category=category)

        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latestPost'] = PostModel.objects.all().order_by('-id')[:1]
        context['postCategories'] = PostCategoryModel.objects.all()
        context['postTags'] = PostTagModel.objects.all()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            html = render_to_string('pages/blog/blog_result.html', {'object_list': context['object_list']}, request=self.request)
            return JsonResponse({'success': True, 'html': html, 'paginator': context['paginator'].num_pages, 'page': context['page_obj'].number})
        return super().render_to_response(context, **response_kwargs)


class blogdetail(DetailView):
    model = PostModel
    template_name = "pages/blog/blogdetail.html"  
    
    def get_queryset(self):
        return PostModel.objects.select_related('category') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.get_object()

        similar_posts = PostModel.objects.filter(
            Q(category=current_post.category) | Q(tags__in=current_post.tags.all())
        ).exclude(id=current_post.id).distinct()[:2].select_related('category')
        
        context['similarPosts'] = similar_posts
        return context 

class job(ListView):
    model = JobModel
    template_name = "pages/job/job.html"    

    def get_queryset(self):
        return JobModel.objects.select_related('category')

class JobDetailView(DetailView):
    model = JobModel
    template_name = "pages/job/jobdetail.html"

    def get_queryset(self):
        return JobModel.objects.select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_job = self.object
        context['other_jobs'] = JobModel.objects.filter(category=current_job.category).exclude(pk=current_job.pk).select_related('category')[:3]
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


class ProjectsView(TemplateView):
    template_name = 'pages/projects/projects.html'

    def get_queryset(self):
        category = self.request.GET.get("category", '')
        projects = ProjectModel.objects.all().select_related('category')

        if category and category.isdigit():
            if ProjectCategory.objects.filter(id=category).exists():
                projects = projects.filter(category=category)

        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.get_queryset()
        context['categories'] = ProjectCategory.objects.all()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            projects = self.get_queryset()
            html = render_to_string('pages/projects/projects_result.html', {'projects': projects})
            return JsonResponse({'success': True, 'html': html})

        return super().render_to_response(context, **response_kwargs)     
    
class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = 'pages/projects/projectdetail.html'

class MyProfileEdit(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = AccountForm 
    template_name = "pages/user/profile.html"
    success_url = reverse_lazy('main:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile image updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")
        return super().form_invalid(form)
    
def loginView(request):
    template_name = 'pages/user/login.html'
    if request.user.is_authenticated:
        logout(request)
        return redirect('main:index')
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True, 'redirect': reverse('main:profile')})
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
    template_name = 'pages/user/registration.html'
    success_url = reverse_lazy('main:profile')

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data['password'])
        del form.cleaned_data['confirm_password']

        response = super().form_valid(form)
        messages.success(self.request, "You have successfully created an account")
        login(self.request, self.object) 
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        errors = {field: [error for error in form[field].errors] for field in form.fields}
        return JsonResponse({'success': False, 'errors': errors})

class UserPasswordChangeView(PasswordChangeView):
    model = UserModel
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("main:profile")
    template_name = "pages/user/changepassword.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.user.refresh_from_db() 
        self.request.user.updated_at = timezone.now()
        self.request.user.save(update_fields=['updated_at'])
        messages.success(self.request, "Your password was successfully updated")
        return response

def logoutView(request):
    logout(request)
    return redirect('main:index')


# --ERRORS VIEWS-- # 

def PageNotFound(request, *args, **kwargs):
    text = render_to_string('pages/error/error404.html')
    return HttpResponseNotFound(text)