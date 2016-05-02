from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.files import File
from auth.models import UserProfile
from .forms import RegisterForm, LoginForm, SMForm, GroupForm, ForgotPassword, ForgotUsername
from Crypto.PublicKey import RSA
from Crypto import Random
from django.core.mail import EmailMessage
from home.views import index as homepage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper
import os


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

# def create_file(request):

# filename = os.getcwd()+'/auth/key.pem'
# wrapper = FileWrapper(File(filename))
# response = HttpResponse(wrapper, content_type='text/plain')
# response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
# response['Content-Length'] = os.path.getsize(filename)
# return response

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
            security_question = form.cleaned_data['security_question']
            site_manager = False
            if password == confirm:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first,
                                                last_name=last)
                user.save()
                key = key_generation()
                public_key = key.publickey().exportKey()
                private_key = key.exportKey()
                filename = os.getcwd()+'/auth/key.pem'
                f = open(filename,'w')
                f.write(private_key.decode('utf-8'))
                f.close()
                user = User.objects.get(username=username)
                user_profile = UserProfile.objects.create(user=user, username=username, site_manager=site_manager,
                                                          public_key=public_key, security_question=security_question)
                user_profile.save()
                message = 'Hi ' + first + ',\n\nThank you for signing up for SafeCollab!\n\nBest,\nThe SafeCollab Team'
                email = EmailMessage('Welcome to SafeCollab', message, to=[email])
                email.attach_file(filename)
                email.send()
                f = open(filename, 'w+')
                f.close()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return homepage(request)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def list_users(request):
    if not request.user.userprofile.site_manager:
        return homepage(request)
    users = UserProfile.objects.all()
    if request.method == "POST":
        num_sm = UserProfile.objects.filter(site_manager=True).count()
        sm = request.POST.getlist('sm')
        activate = request.POST.getlist('activate')
        if len(sm) + num_sm > 3:
            return render(request, 'sm.html', {
                'users': users,
                'form': SMForm()
            })
        for x in sm:
            u_p = UserProfile.objects.get(username=x)
            u_p.site_manager = True
            u_p.save()
        for y in activate:
            u_p = User.objects.get(username=y)
            status = u_p.is_active
            u_p.is_active = not status
            u_p.save()

    return render(request, 'sm.html', {
        'users': users,
        'form': SMForm()
    })


def manage_group(request):
    groups = Group.objects.all()
    if request.method == "POST":
        remove = request.POST.getlist('remove')
        for group in remove:
            g = Group.objects.get(name=group)
            for user in g.user_set.all():
                g.user_set.remove(user)
    if request.user.userprofile.site_manager:
        groups = Group.objects.all()
    else:
        groups = request.user.groups.all()
    users = User.objects.all()
    return render(request, 'group.html', {
        'groups': groups,
        'users': users,
    })


def show_group(request, name):
    group = Group.objects.get(name=name)
    if request.method == "POST":
        remove = request.POST.getlist('remove')
        for x in remove:
            user = User.objects.get(username=x)
            if user.groups.filter(name=name).exists():
                group.user_set.remove(user)
            else:
                group.user_set.add(user)
    users = group.user_set.all()
    if request.user.userprofile.site_manager:
        all_users = User.objects.all()
    else:
        all_users = User.objects.all()
        for user in users:
            if str(user.username) is not str(request.user.username):
                all_users = all_users.exclude(username=user.username)
    return render(request, 'group_info.html', {
        'users': users,
        'all_users': all_users,
    })


def create_group(request):
    users = User.objects.all()
    users = users.exclude(username=request.user)
    if request.method == "POST":
        name = request.POST.get('group')
        newgroup = Group.objects.create(name=name)
        newgroup.user_set.add(User.objects.get(username=request.user))
        add = request.POST.getlist('add')
        for x in add:
            user = User.objects.get(username=x)
            newgroup.user_set.add(user)
    return render(request, 'create_group.html', {
        'users': users,
        'form': GroupForm()
    })


def change_password(request):
    if request.method == 'POST':
        form = ForgotPassword(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            security_question = form.cleaned_data['security_question']
            user = UserProfile.objects.get(username=username)
            userChange = User.objects.get(username=username)
            if password == confirm and security_question == user.security_question:
                userChange.set_password(password)
                userChange.save()
                message = 'Hi ' + userChange.first_name + ',\n\nYou have successfully changed your password!\n\nBest,\nThe SafeCollab Team'
                email = EmailMessage('Welcome to SafeCollab', message, to=[userChange.email])
                email.send()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return homepage(request)
    else:
        form = ForgotPassword()

    return render(request, 'changepassword.html', {'form': form})


def forgot_username(request):
    username = ''
    if request.method == 'POST':
        form = ForgotUsername(request.POST)
        if form.is_valid():
            last = form.cleaned_data['last']
            email = form.cleaned_data['email']
            user = User.objects.get(email=email, last_name=last)
            username = user.username
    else:
        form = ForgotUsername()

    return render(request, 'forgot.html', {'form': form, 'username': username})
