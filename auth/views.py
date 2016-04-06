from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


def login_user(request):
    logout(request)
    state = "Login to SafeCollab."
    username = password = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return render(request, 'index.html')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'login.html', {'state': state, 'username': username, 'password': password})


def logout_user(request):
    logout(request)
    return render(request, 'index.html')


def index(request):
    if request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')