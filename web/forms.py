from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import UserModel, PostModel, ContactusModel, JobApplyModel, \
CheckOut, FeedbackModel
from django.utils.translation import gettext_lazy as _


# --------------------------------------------------------------------------- #
# User Model Form
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name','user_image', 'company', 'location', 'email', 'position', 'mobileNumber', 'socialMedia']

class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Check if this is a new instance
            self.fields['user'].initial = self.request.user
            self.fields['user'].widget = forms.HiddenInput()

class ContactusModelForm(forms.ModelForm):
    class Meta:
        model = ContactusModel
        exclude = ('user',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ['text',]

class JobApplyForm(forms.ModelForm):
    class Meta:
        model = JobApplyModel
        exclude = ('user',)


    # Ensure that the category field is not marked as required

class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'placeholder': _('Enter your username')
    }))

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'placeholder': _('Enter you password')
    }))

    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user == None:
            raise ValidationError(_('Username or password is incorrect'))
        return cleaned_data

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not same')
        return self.cleaned_data['confirm_password']

    def clean_username(self):
        try:
            user = UserModel.objects.get(username=self.cleaned_data['username'])
            if user:
                raise ValidationError('This username is already in use')
        except:
            return self.cleaned_data['username']
        
class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        exclude = ('item', 'total_price', 'user')
        

