from django.contrib.auth.models import User
import os
import sys
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application
from Crypto.PublicKey import RSA
from Crypto import Random
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import django
import report_database
import urllib.request
import auth

from Crypto.Cipher import ARC4
from Crypto import Random

def encrypt1(file_path, key):
    enc = ARC4.new(key)
    file = str(input("Please enter a file name for encrypted file: "))
    print("encrypt1 function")
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as in_file:
            with open(file, 'wb') as out_file:
                for line in in_file:
                    out_file.write(enc.encrypt(line))
        return True

    return False

def encrypt2(filename, key):
    enc = ARC4.new(key)
    print("encrypt2 function")
    file = str(input("Please enter a file name for encrypted file: "))
    script_dir = os.path.dirname(__file__)
    rel_path = filename
    abs_file_path = os.path.join(script_dir, rel_path)

    if os.path.isfile(abs_file_path):
        with open(abs_file_path, 'rb') as in_file:
            with open(file, 'wb') as out_file:
                for line in in_file:
                    out_file.write(enc.encrypt(line))
        return True

    return False

def decrypt(ref, key):
    page = urllib.request.urlopen(ref)
    document = str(input("Please enter the name you want the decrypted file to be written into"))
    f = open(document, "w")
    content = page.read()
    dec = ARC4.new(key)
    f.write(str(dec.decrypt(content)))
    f.close()
    return True


def login():
    global authorized
    userN = input("Please enter your login username: ")
    passW = input("Please enter your password: ")

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

    alldocs = report_database.models.Documents.objects.all()

    if(auth.models.UserProfile.objects.get(username=userN).site_manager):
        for i in alldocs[0:]:
            files.append((i.docfile, i.encrypt))
    else:
        for i in alldocs[0:]:
            if not i.private:
                files.append((i.docfile, i.encrypt))
            else:
                sharedUsers = User.objects.filter(documents=i.pk)
                print("in one file %s" % i.docfile)
                for t in sharedUsers:
                    #print("inside shared user check")
                    print(t)
                    if str(userN) == str(t):
                        #print("this is true~")
                        files.append((i.docfile, i.encrypt))

    print("\nHere are your files:\n")
    index = 1
    for i in files:
        print("file %s : %s" % (index, i[0]))
        index += 1

    print("\nPlease enter one of the following commands: ")
    print("exit -> this command exits out of the FDA")
    print("download (file number) -> this command downloads file and decrypts it if it is encrypted")
    print("encrypt1 (path to file) -> this command encrypts a file in any location")
    print("encrypt2 (file name) -> this command encrypts a file located in current directory\n")

    ###going to download reports###
    while True:
        text = input()
        if text == "exit":
            break

        words = text.split()
        if not len(words) is 2 and not len(words) is 0:
            print("You have not entered a valid command")
        else:
            if words[0] == "download":
                #print("download")

                if files[int(words[1])-1][1]:
                    print("This files is encrypted")
                    key = input("Please enter key to decrypt: ")
                    ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1][0])
                    #for heroku
                    #ref = "https://agile-earth-28935.herokuapp.com/"+str(files[int(words[1])-1][0])
                    if not decrypt(ref, key):
                        print("Your key is not correct")
                    else:
                        print("You have successfully downloaded file %s" % words[1])

                else:
                    ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1][0])
                    #print(ref)
                    #for heroku
                    #ref = "https://agile-earth-28935.herokuapp.com/"+str(files[int(words[1])-1][0])
                    download = str(files[int(words[1])-1][0])
                    #print(download)
                    urllib.request.urlretrieve(ref, download[10:])
                    print("You have downloaded file %s" % words[1])
            elif words[0] == "encrypt1":
                #print("encrypt1")
                key = input("Please enter key to encrypt: ")
                if not encrypt1(words[1], key):
                    print("You have not entered a valid file")
                else:
                    print("Encryption successful! You're file is in the current directory.")
            elif words[0] == "encrypt2":
                #print("encrypt2")
                key = input("Please enter key to encrypt: ")
                if not encrypt2(words[1],key):
                    print("You have not enetered a valid file")
                else:
                    print("Encryption successful! You're file is in the current directory.")
            else:
                print("You have not entered a valid command")


def login2():
    global authorized
    userN = input("Please enter your login username: ")
    passW = input("Please enter your password: ")

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

    #alldocs = report_database.models.Documents.objects.all()

    reports = report_database.models.Report.objects.all()

    user_reports = []

    if(auth.models.UserProfile.objects.get(username=userN).site_manager):
        for i in reports[0:]:
            user_reports.append(i.report_name)
    else:
        for i in reports[0:]:
            if not i.private:
                user_reports.append(i.report_name)
            else:
                sharedUsers = User.objects.filter(report=i.pk)
                #print("name: %s" % i.report_name)
                if(str(i.creator) == str(userN)) :
                    user_reports.append(i.report_name)
                for t in sharedUsers:
                    #print("in list of sharedUser")
                    #print(str(t))
                    if str(userN) == str(t):
                        print("this is user is owns this report")
                        user_reports.append(i.report_name)

    print("\nHere are your reports:\n")
    index = 1
    for i in user_reports:
        print("report %s : %s" % (index, i))
        index += 1


    print("\nPlease enter one of the following commands: ")
    print("exit -> this command exits out of the FDA")
    print("enter (report number) -> this command enters the report and lists all the files\n")

    while(True):
        text = input()
        if text == "exit":
            break

        words = text.split()
        if not len(words) is 2 and not len(words) is 0:
            print("You have not entered a valid command or valid arguments")
        else:
            if words[0] == "enter":
                if int(words[1]) > 0 and int(words[1]) <= len(user_reports):
                    reportN = user_reports[int(words[1])-1] #gets report name
                    rep = report_database.models.Report.objects.get(report_name=reportN)
                    file_list = report_database.models.Documents.objects.filter(report=rep)
                    listfiles(file_list)
                else:
                    print("You have not enetered a valid report number")
            else:
               print("You have not entered a valid command or valid arguments")


def listfiles(file_list):

    files = [];

    for i in file_list:
        files.append((i.docfile, i.encrypt))

    print("\nHere are your files:\n")
    index = 1
    for i in files:
        print("file %s : %s" % (index, i[0]))
        index += 1

    print("\nPlease enter one of the following commands: ")
    print("return -> this command returns to the list of reports")
    print("download (file number) -> this command downloads file and decrypts it if it is encrypted")
    print("encrypt1 (path to file) -> this command encrypts a file in any location")
    print("encrypt2 (file name) -> this command encrypts a file located in current directory\n")

    ###going to download reports###
    while True:
        text = input()
        if text == "return":
            print("You have return to reports list")
            break

        words = text.split()
        if not len(words) is 2 and not len(words) is 0:
            print("You have not entered a valid command")
        else:
            if words[0] == "download":
                #print("download")

                if files[int(words[1])-1][1]:
                    print("This files is encrypted")
                    key = input("Please enter key to decrypt: ")
                    ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1][0])
                    #for heroku
                    #ref = "https://agile-earth-28935.herokuapp.com/"+str(files[int(words[1])-1][0])
                    if not decrypt(ref, key):
                        print("Your key is not correct")
                    else:
                        print("You have successfully downloaded file %s" % words[1])

                else:
                    ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1][0])
                    #print(ref)
                    #for heroku
                    #ref = "https://agile-earth-28935.herokuapp.com/"+str(files[int(words[1])-1][0])
                    download = str(files[int(words[1])-1][0])
                    #print(download)
                    urllib.request.urlretrieve(ref, download[10:])
                    print("You have downloaded file %s" % words[1])
            elif words[0] == "encrypt1":
                #print("encrypt1")
                key = input("Please enter key to encrypt: ")
                if not encrypt1(words[1], key):
                    print("You have not entered a valid file")
                else:
                    print("Encryption successful! You're file is in the current directory.")
            elif words[0] == "encrypt2":
                #print("encrypt2")
                key = input("Please enter key to encrypt: ")
                if not encrypt2(words[1],key):
                    print("You have not enetered a valid file")
                else:
                    print("Encryption successful! You're file is in the current directory.")
            else:
                print("You have not entered a valid command")
    return True


if __name__ == "__main__":
    django.setup()
    proj_path = "/Users/jisukim/Desktop/cs3240-s16-team3/SafeCollab"
    sys.path.append(proj_path)
    application = get_wsgi_application()
    os.environ['DJANGO_SETTINGS_MODULE'] = 'SafeCollab.settings'
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafeCollab.settings")
    #setup_environ(settings)
    #settings.configure()
    print("Welcome to the fda!")
    login2()
