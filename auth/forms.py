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
    security_question = forms.CharField(label='What is the street you grew up on?', max_length=30,
                                        widget=forms.PasswordInput())


class ForgotUsername(forms.Form):
    email = forms.EmailField(label='Email', max_length=50)


class ForgotPassword(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    security_question = forms.CharField(label='What is the street you grew up on?', max_length=30,
                                        widget=forms.PasswordInput())
    password = forms.CharField(label='New Password', widget=forms.PasswordInput())
    confirm = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput())


class SMForm(forms.Form):
    site_manager = forms.BooleanField(label='Site Manager')


class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group Name', max_length=120)
