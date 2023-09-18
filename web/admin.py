# --------------------------------------------------------------------------- #
# Django exceptions
from django.contrib import admin
# --------------------------------------------------------------------------- #
# Models and Forms
from .models import UserModel, PricingModel, PostModel, FeedbackModel, ContactusModel
from .forms import PostModelForm
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _
# --------------------------------------------------------------------------- #
# For saving html code
from django.utils.safestring import mark_safe
from django import forms


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(PricingModel)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'price']
    list_display_links = ['id', 'type', 'price']
    search_fields = ['type', 'price']

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    readonly_fields = ('user',)

    def get_fieldsets(self, request, obj=None):
        if obj:
            return super().get_fieldsets(request, obj)
        else:
            return (
                (None, {'fields': ('title', 'image', 'short_description', 'post_text')}),
            )

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not obj.user_id:
            obj.user = request.user
        return obj
    
@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = ['id', 'text']
    search_fields = ['text']

@admin.register(ContactusModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'company']
    list_display_links = ['id', 'company']
    search_fields = ['company']

admin.site.site_header = 'Cyber Code'
admin.site.site_title = 'Cyber Code'