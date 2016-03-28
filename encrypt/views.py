from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random

def secret_string(str, key):
    """
    :param str: Passes in a string to encrypt
    :param key: Uses a public key for encryption
    :return: returns an encrypted string in byte form
    """
    public_key = key.publickey()
    bytestr = str.encode('utf-8')
    enc_data = public_key.encrypt(bytestr, 32)
    return enc_data[0]

def index(request):
    if request.method == "POST" and request.POST.get("unencryptedtext") != None:
        unencrypted_text = request.POST.get("unencryptedtext")
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        data = secret_string(unencrypted_text, key)
        data = str(data)
        return render(request, 'encryption.html',{
                      'data':data ,
                        'key':key
        })
    else:
        return render(request, 'encryption.html')
# Create your views here.
