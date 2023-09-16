# --------------------------------------------------------------------------- #
# Django exceptions
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# --------------------------------------------------------------------------- #
# Models
from .models import UserModel, PostModel
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _
from django import forms

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Form
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email']

class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Check if this is a new instance
            self.fields['user'].initial = self.request.user
            self.fields['user'].widget = forms.HiddenInput()
