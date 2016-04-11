from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password')


class RegisterForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password')
    confirm = forms.CharField(label='Confirm Password')