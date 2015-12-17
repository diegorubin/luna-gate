from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)

    def save(self):
        user = User()
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()

