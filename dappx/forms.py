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

    def clean_Username(self): # Validates the Username Field
        Username = self.cleaned_data.get('Username')
        if (Username == ""):
            raise forms.ValidationError('This field cannot be left blank.')
        for instance in NewAccount.objects.all():
            if instance.Username == Username:
                raise forms.ValidationError('Username already exists. Please try again.')
        return Username

    # class UserProfileInfoForm(forms.ModelForm):
    #     class Meta():
    #         model = UserProfileInfoForm
    #         fields = ('portfolio_site','profile_pic')