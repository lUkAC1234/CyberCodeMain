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