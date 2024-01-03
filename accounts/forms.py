from django import forms
from phonenumber_field.formfields import PhoneNumberField

class UserRegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = PhoneNumberField(region="IR", label="Phone Number")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = PhoneNumberField(region="IR")
    password = forms.CharField(widget=forms.PasswordInput)
