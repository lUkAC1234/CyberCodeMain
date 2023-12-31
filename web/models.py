from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import os

class EnglishLettersUsernameValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9]{8,16}$'
    message = _(
        'Username can only contain lowercase English letters (a-z) and numbers (0-9), and must be between 8 and 16 characters long.'
    )
    flags = 0

    def __call__(self, value):
        super().__call__(value)
        return value.lower()

class PasswordValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9!$@%]{8,128}$'
    message = _(
        'Password must be at least 8 characters and at most 128 characters long, and can only contain English letters, numbers and !$@%.'
    )
    flags = 0

class PhoneValidator(RegexValidator):
    regex=r'^\+\d{12}$'
    message =_("Phone number must be in the format: '+123456789012'.")

    flags = 0

def validate_image_extension(value):
    allowed_extensions = ['.webp', '.png', '.jpg', '.jpeg', '.svg', '.jfif']
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in allowed_extensions:
        raise ValidationError(_('User image: Unsupported file extension. Please upload a webp, png, jpg, jpeg, or svg file.'))
# --------------------------------------------------------------------------- #
# Users
class UserModel(AbstractUser):
    user_image = models.FileField(
        upload_to='users/profile/profile-image/%Y/%m/%d/',
        default='default-user.jpg',
        validators=[validate_image_extension]
    )
    company = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    mobileNumber = models.CharField(max_length=13, blank=True, null=True)  # Assuming you have a PhoneValidator
    socialMedia = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    
    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=False,
        help_text=_('Required. Must be a valid email address.'),
        validators=[EmailValidator(message=_('Enter a valid email address.'))],
    )

    username = models.CharField(
        _('username'),
        max_length=16,
        unique=True,
        help_text=_('Required. Up to 16 characters. Only English letters (a-z)(0-9).'),
        validators=[EnglishLettersUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    password = models.CharField(
        _('password'),
        max_length=128, 
        validators=[PasswordValidator()],
        help_text=_("Password must be at least 8 characters and at most 32 characters long, and can only contain English letters, numbers and !$@%."),
    )

    def save(self, *args, **kwargs):
        # Ensure the email is unique before saving
        if UserModel.objects.filter(email=self.email).exclude(id=self.id).exists():
            raise ValidationError({'email': _('A user with that email already exists.')})

        # Your existing save logic here
        if self._state.adding or not self.updated_at:
            self.updated_at = timezone.now()

        self.username = self.username.lower()
        super().save(*args, **kwargs)
    
# --------------------------------------------------------------------------- #


class PricingModel(models.Model):
    type = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    advantages = RichTextField()
    popular = models.BooleanField(null=True)
    recommended = models.BooleanField(null=True)

    @staticmethod
    def get_cart_objects(cart_list):
        unique_cart_list = list(set(cart_list))

        qs = PricingModel.objects.filter(id__in=unique_cart_list)

        pricing_dict = {pricing.id: pricing for pricing in qs}

        cart_objects = [pricing_dict[cart_id] for cart_id in unique_cart_list if cart_id in pricing_dict]

        return cart_objects

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'
        ordering = ('-id',)

    def __str__(self):
        return self.type

class PostCategoryModel(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category
    
    def post_count(self):
        return PostModel.objects.filter(category=self).count()
    
class PostTagModel(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag
    
    def post_count(self):
        return PostModel.objects.filter(tags=self).count()

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/posts/images/%Y/%m/%d/')
    short_description = models.TextField()
    post_text = RichTextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategoryModel, on_delete=models.CASCADE, related_name='postCategories')
    tags = models.ManyToManyField(PostTagModel, related_name='postTags')
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='postUser')
    is_private = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    
class FeedbackModel(models.Model):
    text = models.TextField(max_length=2500)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='feedbackUser')
    created_at = models.DateTimeField(auto_now_add=True)
    is_allowed = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ('-id',)

    def __str__(self):
        return self.text
    
class ContactusModel(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, validators=[PhoneValidator()])
    email = models.EmailField(max_length=50)
    company = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='contactUser')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('-id',)

    def __str__(self):
        return self.fullname
    
class FaqModel(models.Model):
    question = models.CharField()
    answer = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQS'
        ordering = ('-id',)

    def __str__(self):
        return self.question
    
class JobCategoryModel(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category
    
class JobKnowledgesModel(models.Model):
    knowledge = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.knowledge 

class JobModel(models.Model):
    title = models.CharField()
    description = models.TextField()

    aboutthejob = RichTextField()
    responsibilities = RichTextField()
    requirements = RichTextField()

    category = models.ForeignKey(JobCategoryModel, on_delete=models.CASCADE)
    knowledge = models.ManyToManyField(JobKnowledgesModel, related_name='jobKnowledges')
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(default='Uzbekistan, Tashkent')

    class Meta:
        verbose_name = 'Jobs Openings'
        verbose_name_plural = 'Jobs Openings'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    
class JobApplyModel(models.Model):
    firstName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[PhoneValidator()])
    text = models.TextField(max_length=1000)
    category = models.ForeignKey(JobCategoryModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='jobApplyUser')
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectCategory(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Projects Categories'
        verbose_name_plural = 'Projects Categories'
        ordering = ('-id',)

class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/images/%Y/%m/%d/')
    link = models.URLField()
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    users = models.ManyToManyField(UserModel)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'
        ordering = ('-id',)
    
class PartnersModel(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=f'partners/logos/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    

class CheckOut(models.Model):
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, validators=[PhoneValidator()])
    email = models.EmailField()
    item = models.ManyToManyField(PricingModel, related_name='checkout')
    total_price = models.FloatField()
    socail_media = models.URLField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='checkoutUser')
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=0)
    is_completed = models.BooleanField(default=0)
    success_checkout = models.BooleanField(default=0)

    def str(self):
        return f"{self.first_name} {self.total_price}$"

    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkout'
