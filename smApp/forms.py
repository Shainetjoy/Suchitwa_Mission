from django.contrib.auth.forms import UserCreationForm
from django import forms
from smApp.models import User,Customer
from django.contrib.auth.password_validation import validate_password



class UserRegistration(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The two password fields didn't match.")
            # You can add custom password complexity checks here
            try:
                validate_password(password2)
            except forms.ValidationError as error:
                # Catch the ValidationError and handle it as per your requirement
                raise forms.ValidationError("Password complexity requirement not met.")
        return password2
    class Meta:
        model = User
        fields = ('username','password1','password2')


class CustomerRegistration(forms.ModelForm):

    class Meta:
        model = Customer
        exclude =('user','approve')