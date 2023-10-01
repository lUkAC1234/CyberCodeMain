from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class EnglishLettersUsernameValidator(RegexValidator):
    regex = r'^[a-z0-9]{8,16}$'
    message = _(
        'Username can only contain lowercase English letters (a-z) and numbers (0-9), and must be between 8 and 16 characters long.'
    )
    flags = 0

class PhoneValidator(RegexValidator):
    regex=r'^\+\d{12}$'
    message =_("Phone number must be in the format: '+123456789012'.")

    flags = 0

# --------------------------------------------------------------------------- #
# Users
class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to=' users/profile/profile-image/%Y/%m/%d/', default='default-user.jpg')
    company = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    mobileNumber = models.CharField(max_length=13, blank=True, null=True, validators=[PhoneValidator()])
    socialMedia = models.URLField(blank=True, null=True)

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
# --------------------------------------------------------------------------- #


class PricingModel(models.Model):
    type = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    advantages = RichTextField()
    popular = models.BooleanField(null=True)
    recommended = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'
        ordering = ('-id',)

    def __str__(self):
        return self.type

class PostCategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
class PostTagModel(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/posts/images/%Y/%m/%d/')
    short_description = models.TextField()
    post_text = RichTextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategoryModel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(PostTagModel, related_name='postTags')
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='postUser')

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
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQS'
        ordering = ('-id',)

    def __str__(self):
        return self.question
    
class JobCategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
class JobModel(models.Model):
    title = models.CharField()
    description = models.TextField()

    aboutthejob = RichTextField()
    responsibilities = RichTextField()
    requirements = RichTextField()

    category = models.ForeignKey(JobCategoryModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'JOB OPENINGS'
        verbose_name_plural = 'JOBS OPENINGS'
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
    
class PartnersModel(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=f'partners/logos/%Y/%m/%d/')

    class Meta:
        verbose_name = 'PARTNER'
        verbose_name_plural = 'PARTNERS'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    
class PaymentModel(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[PhoneValidator()])
    text = models.TextField(max_length=1000)
    category = models.ForeignKey(PricingModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='pricingApplyUser')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'PAYMENT'
        verbose_name_plural = 'PAYMENTS'
        ordering = ('-id',)

    def __str__(self):
        return self.first_name   
    
class ShoppingCartItem(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(PricingModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s {self.product.type}"

    def total_price(self):
        return self.product.price * self.quantity