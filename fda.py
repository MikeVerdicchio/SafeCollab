from django.contrib.auth.models import User
import os
import sys
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application
from Crypto.PublicKey import RSA
from Crypto import Random
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
#from django.core.management import setup_environ
import django
from report_database.models import Report


def login():
    global authorized
    userN = input("Please enter your login username: ")
    passW = input("Please enter your password: ")
    
    #print(username)
    #print(password)
    user = authenticate(username=userN, password=passW)
    if user is not None:
        if user.is_active:
            #print("User is valid\n")
            #login(, user)
            authorized = True


    else:
        authorized = False


def reports():
    report = Report.objects.all()
    for i in report[0:]:
    

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafeCollab.settings")
    application = get_wsgi_application()
    django.setup()
    #setup_environ(settings)
    login();
