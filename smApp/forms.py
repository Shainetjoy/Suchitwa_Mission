from django.contrib.auth.forms import UserCreationForm
from django import forms
from smApp.models import User,Customer

class UserRegistration(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password1','password2')


class CustomerRegistration(forms.ModelForm):

    class Meta:
        model = Customer
        exclude =('user',)