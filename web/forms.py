# --------------------------------------------------------------------------- #
# Django exceptions
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# --------------------------------------------------------------------------- #
# Models
from .models import UserModel
# --------------------------------------------------------------------------- #
# Translation
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# User Model Form
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email']