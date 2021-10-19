from django import forms
from django.contrib.auth.models import User
from restaurant_app.models import UserProfileInfo
from restaurant_app.models import orders

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('email','username','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
