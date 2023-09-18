from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
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

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ('-id',)

    def __str__(self):
        return self.text
    
class ContactusModel(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    company = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='contactUser')