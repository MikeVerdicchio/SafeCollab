#from django.contrib.auth.models import User
import os
import sys
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application
from Crypto.PublicKey import RSA
from Crypto import Random
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import setup_environ
import django
#from report_database.models import Report
import report_database
import urllib.request

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

    if not authorized:
        print("You have not entered a valid username and password")
        sys.exit()
    files = []
    documents = report_databse.models.Documents.objects.all()

    for i in documents[0:]:
        if not i.private: #if public file list
            files.append(i.docfile)
        else:
            if userN in i.shared_user:
                files.append(i.docfile)


    #report = report_database.models.Report.objects.all()
    #print("in reports\n")
    #for i in report[0:]:
        #print("in loop reports\n")
        #if i.file_1:
         #   files.append(i.file_1)
          #  print("file 1 exists")
        #if i.file_2:
         #   files.append(i.file_2)
          #  print("file 2 exists")
        #if i.file_3:
         #   files.append(i.file_3)
          #  print("file 3 exists")

    print("Here are your files:")
    index = 1
    for i in files:
        print("file %s : %s" % (index, i))
        index += 1

    ###going to download reports###
    while True:
        text = input()
        if text == "exit":
            break
        words = text.split()
        if words[0] == "download":
            #download file
            #print("you need to download file")
            #for local server
            ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1])
            #for heroku
            #ref = "https://agile-earth-28935.herokuapp.com/"+str(files[int(words[1])-1])
            #print("http://127.0.0.1:8000/media/"+str(files[int(words[1])-1]))
            #print("yes")
            download = str(files[int(words[1])-1])
            #print(download[10:])
            urllib.request.urlretrieve(ref, download[10:])
            print("you have downloaded file %s" % words[1])

def login2():
    global authorized
    userN = input("Please enter your login username: ")
    passW = input("Please enter your password: ")

    #print(username)
    #print(password)
    user = authenticate(username=userN, password=passW)
    if user is not None:
        if user.is_active:
            authorized = True

    else:
        authorized = False

    if not authorized:
        print("You have not entered a valid username and password")
        sys.exit()
    files = []

    alldocs = Documents.objects.all()

    for i in alldocs[0:]:
        if not i.private:
            files.append(i.docfile)
        else:
            if userN in i.shared_user:
                files.append(i.docfile)

    print("Here are your files:")
    index = 1
    for i in files:
        print("file %s : %s" % (index, i))
        index += 1

    ###going to download reports###
    while True:
        text = input()
        if text == "exit":
            break
        words = text.split()
        if words[0] == "download":
            #download file

            #for local server
            ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1])
            #for heroku
            #ref = "https://agile-earth-28935.herokuapp.com/"+str(files[int(words[1])-1])
            download = str(files[int(words[1])-1])
            urllib.request.urlretrieve(ref, download[10:])
            print("you have downloaded file %s" % words[1])

if __name__ == "__main__":
    proj_path = "/Users/jisukim/Desktop/cs3240-s16-team3/SafeCollab"
    sys.path.append(proj_path)
    application = get_wsgi_application()
    django.setup()
    os.environ['DJANGO_SETTINGS_MODULE'] = 'SafeCollab.settings'
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafeCollab.settings")
    #setup_environ(settings)
    #settings.configure()
    login()
