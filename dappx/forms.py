# dappx/forms.py from django import forms
# from dappx.models import UserProfileInfoForm

from django import forms
from .models import NewAccount
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class RecordsForm(forms.ModelForm):
    class Meta:
        model = NewAccount
        fields = "__all__"
        
    # class UserProfileInfoForm(forms.ModelForm):
    #     class Meta():
    #         model = UserProfileInfoForm
    #         fields = ('portfolio_site','profile_pic')