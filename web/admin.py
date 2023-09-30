# --------------------------------------------------------------------------- #
# Django exceptions
from django.contrib import admin
# --------------------------------------------------------------------------- #
# Models and Forms
from .models import UserModel, PricingModel, PostModel, FeedbackModel, ContactusModel, \
FaqModel, JobModel, JobCategoryModel, PostTagModel, PostCategoryModel, PartnersModel, \
JobApplyModel, PaymentModel
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
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    readonly_fields = ('user', 'posted_on')

    def get_fieldsets(self, request, obj=None):
        if obj:
            return super().get_fieldsets(request, obj)
        else:
            return (
                (None, {'fields': ('title', 'image', 'short_description', 'post_text', 'category', 'tags')}),
            )

    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not obj.user_id:
            obj.user = request.user
        return obj
    
@admin.register(PostTagModel)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    list_display_links = ['id', 'tag']
    search_fields = ['tag']

@admin.register(PostCategoryModel)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']
    
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
    readonly_fields = ['created_at']

@admin.register(FaqModel)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    list_display_links = ['id', 'question']
    search_fields = ['question']

@admin.register(JobModel)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(JobCategoryModel)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']

@admin.register(JobApplyModel)
class JobApplyyAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName']
    list_display_links = ['id', 'firstName']
    search_fields = ['firstName']
    readonly_fields = ['created_at']

@admin.register(PartnersModel)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name']

admin.site.site_header = 'Cyber Code'
admin.site.site_title = 'Cyber Code'