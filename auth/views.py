from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from auth.models import UserProfile
from .forms import RegisterForm, LoginForm
from Crypto.PublicKey import RSA
from Crypto import Random

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    state = "You're successfully logged in!"
                    return render(request, 'index.html')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def key_generation():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    return key

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first']
            last = form.cleaned_data['last']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            site_manager = False
            if password == confirm:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first, last_name=last)
                user.save()
                key = key_generation()
                public_key = key.publickey().exportKey('PEM')
                user_profile = UserProfile.objects.create(username=username, site_manager=site_manager, public_key=public_key)
                user_profile.save()
                return render(request, 'index.html')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

