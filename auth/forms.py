from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    first = forms.CharField(label='First Name', max_length=30)
    last = forms.CharField(label='Last Name', max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())


