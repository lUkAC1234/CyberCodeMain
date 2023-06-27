# --------------------------------------------------------------------------- #
# Django exceptions
from django.contrib import admin
# --------------------------------------------------------------------------- #
# Models and Forms
from .models import UserModel
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