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
import requests
from bs4 import BeautifulSoup
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


def login2():
    global authorized
    userN = input("Please enter your login username: ")
    passW = input("Please enter your password: ")
    url = 'https://agile-earth-28935.herokuapp.com/login/'
    urlcheck = 'http://agile-earth-28935.herokuapp.com/reports/manage/'
    global client
    client = requests.session()
    client.get(url)
    token = client.cookies['csrftoken']
    payload = {'username': userN, 'password': passW, 'csrfmiddlewaretoken': token}
    loginrequest = client.post(url, data=payload, headers={'Referer': url})
    if loginrequest.url == urlcheck:
        authorized = True
    else:
        authorized = False

    if not authorized:
        print("You have not entered a valid username and password")
        sys.exit()
    files = []

    reportsrequest = client.get(urlcheck)
    soup = BeautifulSoup(reportsrequest.text, "html.parser")
    table = soup.find("table")

    reports = report_database.models.Report.objects.all()
    # user_reports = []
    report_names = []
    report_links = []

    # if (auth.models.UserProfile.objects.get(username=userN).site_manager):
    #     for i in reports[0:]:
    #         user_reports.append(i.report_name)
    # else:
    for row in table.find_all("tr")[1:]:
        for data in row.find_all("td")[1:2]:
            report_name = data.get_text()
        for links in row.find_all("a")[1:2]:
            link = 'https://agile-earth-28935.herokuapp.com' + links.get('href')
        report_names.append(report_name)
        report_links.append(link)


        # for i in reports[0:]:
        # if not i.private:
        #     user_reports.append(i.report_name)
        #     sharedUsers = User.objects.filter(report=i.pk)
        # print("name: %s" % i.report_name)
        # if (str(i.creator) == str(userN)):
        #     user_reports.append(i.report_name)
        # for t in sharedUsers:
        #     # print("in list of sharedUser")
        #     # print(str(t))
        #     if str(userN) == str(t):
        #         print("this is user is owns this report")
        #         user_reports.append(i.report_name)

    print("\nHere are your reports:\n")
    index = 1
    for i in report_names:
        print("report %s : %s" % (index, i))
        index += 1

    print("\nPlease enter one of the following commands: ")
    print("exit -> this command exits out of the FDA")
    print("enter (report number) -> this command enters the report and lists all the files")
    print("encrypt1 (path to file) -> this command encrypts a file in any location")
    print("encrypt2 (file name) -> this command encrypts a file located in current directory\n")

    while (True):
        text = input()
        if text == "exit":
            break

        words = text.split()
        if not len(words) is 2 and not len(words) is 0:
            print("You have not entered a valid command or valid arguments")
        else:
            if words[0] == "enter":
                if int(words[1]) > 0 and int(words[1]) <= len(report_names):
                    unencrypted = []
                    encrypted = []
                    filesrequest = client.get(report_links[int(words[1]) - 1])
                    soup = BeautifulSoup(filesrequest.text, "html.parser")
                    try:
                        x = soup.find(id="unencrypted")
                        for li in x.find_all('li'):
                            for a in li.find_all('a'):
                                unencrypted.append('https://agile-earth-28935.herokuapp.com' + a.get('href'))
                    except:
                        print("Woops! There are no unencrypted files.")

                    try:
                        x = soup.find(id="encrypted")
                        for li in x.find_all('li'):
                            encrypted.append('https://agile-earth-28935.herokuapp.com' + '/media/' + li.get_text())
                    except:
                        print("Woops! There are no encrypted files.")

                    if unencrypted == [] and encrypted == []:
                        print("There are no files!")
                    else:
                        listfiles(unencrypted, encrypted)
                else:
                    print("You have not entered a valid report number")
            elif words[0] == "encrypt1":
                # print("encrypt1")
                key = input("Please enter key to encrypt: ")
                if not encrypt1(words[1], key):
                    print("You have not entered a valid file")
                else:
                    print("Encryption successful! You're file is in the current directory.")
            elif words[0] == "encrypt2":
                # print("encrypt2")
                key = input("Please enter key to encrypt: ")
                if not encrypt2(words[1], key):
                    print("You have not enetered a valid file")
                else:
                    print("Encryption successful! You're file is in the current directory.")
            else:
                print("You have not entered a valid command or valid arguments")


def listfiles(unencrypted, encrypted):
    print("\nHere are your unencrypted files:\n")
    index = 1
    cutoff = 0
    for i in unencrypted:
        print("file %s : %s" % (index, i))
        index += 1
    cutoff = index
    print("\nHere are your encrypted files:\n")
    for i in encrypted:
        print("file %s : %s" % (index, i))
        index += 1

    print("\nPlease enter one of the following commands: ")
    print("return -> this command returns to the list of reports")
    print("download (file number) -> this command downloads file and decrypts it if it is encrypted")
    #print("encrypt1 (path to file) -> this command encrypts a file in any location")
    #print("encrypt2 (file name) -> this command encrypts a file located in current directory\n")

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
                # print("download")

                if int(words[1]) >= cutoff:
                    print("This files is encrypted")
                    key = input("Please enter key to decrypt: ")
                    # ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1][0])
                    # for heroku
                    ref = encrypted[int(words[1]) - cutoff]
                    print(ref)
                    page = client.get(ref)
                    document = str(input("Please enter the name you want the decrypted file to be written into: "))
                    dec = ARC4.new(key)
                    with open(document, 'wb') as f:
                        for chunk in page.iter_content(chunk_size=512):
                            f.write(dec.decrypt(chunk))
                    print("You have successfully downloaded file %s" % words[1])

                else:
                    # ref = "http://127.0.0.1:8000/media/"+str(files[int(words[1])-1][0])
                    # print(ref)
                    # for heroku
                    ref = unencrypted[int(words[1]) - 1]
                    download = "Download"
                    # print(download)
                    file = client.get(ref)
                    new = ref.split("/")
                    name = new[5]
                    with open(name, 'wb') as f:
                        for chunk in file.iter_content(chunk_size=512):
                            f.write(chunk)
                    # urllib.request.urlretrieve(ref, download)
                    print("You have downloaded file %s" % words[1])
            else:
                print("You have not entered a valid command")
    return True


if __name__ == "__main__":
    django.setup()
    proj_path = "/Users/jisukim/Desktop/cs3240-s16-team3/SafeCollab"
    sys.path.append(proj_path)
    application = get_wsgi_application()
    os.environ['DJANGO_SETTINGS_MODULE'] = 'SafeCollab.settings'
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafeCollab.settings")
    # setup_environ(settings)
    # settings.configure()
    print("Welcome to the fda!")
    login2()
