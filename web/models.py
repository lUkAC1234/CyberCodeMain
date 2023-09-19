from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
# --------------------------------------------------------------------------- #
# Users
class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to=' users/profile/profile-image/%Y/%m/%d/', default='profile.svg')
    company = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    mobileNumber = models.CharField(max_length=16, blank=True, null=True)
    socialMedia = models.URLField(blank=True, null=True)
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

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/posts/images/%Y/%m/%d/')
    short_description = models.TextField()
    post_text = RichTextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='postUser')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    
class FeedbackModel(models.Model):
    text = models.TextField()
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
    phone_regex = RegexValidator(
        regex=r'^\+\d{12}$',
        message="Phone number must be in the format: '+123456789012'."
    )
    phone = models.CharField(max_length=13, validators=[phone_regex])
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

    category = models.ForeignKey(JobCategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'JOB OPENINGS'
        verbose_name_plural = 'JOBS OPENINGS'
        ordering = ('-id',)

    def __str__(self):
        return self.title