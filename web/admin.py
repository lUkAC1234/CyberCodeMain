# --------------------------------------------------------------------------- #
# Django exceptions
from django.contrib import admin
# --------------------------------------------------------------------------- #
# Models and Forms
from .models import UserModel, PostModel
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _
# --------------------------------------------------------------------------- #
# For saving html code
from django.utils.safestring import mark_safe


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']