from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets={
            'username':forms.TextInput(attrs={'class': 'input'})
        }