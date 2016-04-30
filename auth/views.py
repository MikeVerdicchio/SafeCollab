from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.files import File
from auth.models import UserProfile
from .forms import RegisterForm, LoginForm, SMForm, GroupForm
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

#def create_file(request):

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
            site_manager = False
            if password == confirm:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first,
                                                last_name=last)
                user.save()
                key = key_generation()
                public_key = key.publickey().exportKey()
                print(public_key)
                private_key = key.exportKey()
                print(private_key)
                filename = os.getcwd()+'/auth/key.pem'
                f = open(filename,'wb')
                f.write(private_key)
                user = User.objects.get(username=username)
                user_profile = UserProfile.objects.create(user=user, username=username, site_manager=site_manager,
                                                          public_key=public_key)
                user_profile.save()
                message = 'Hi ' + first + ',\n\nThank you for signing up for SafeCollab!\n\nBest,\nThe SafeCollab Team'
                email = EmailMessage('Welcome to SafeCollab', message, to=[email])
                email.attach_file(filename, "application/text")
                email.send()
                f = open(filename,'w+')
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
            all_users = all_users.exclude(username=user.username)
    return render(request, 'group_info.html', {
        'users': users,
        'all_users': all_users,
    })

def create_group(request):
    users = User.objects.all()
    if request.method == "POST":
        name = request.POST.get('group')
        newgroup = Group.objects.create(name=name)
        add = request.POST.getlist('add')
        for x in add:
            user = User.objects.get(username=x)
            newgroup.user_set.add(user)
    return render(request, 'create_group.html', {
        'users': users,
        'form': GroupForm()
    })
