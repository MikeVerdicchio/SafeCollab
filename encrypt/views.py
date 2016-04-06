from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
counter = 0

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


def decode_string(bytestr, bytekey):
    """
    :param bytestr: Passes in a bytearray to decode
    :param bytekey: Passes in a bytearray used for decoding
    :return: returns a decoded bytearray
    """
    IV = 16 * '\x00'
    mode = AES.MODE_CBC
    keyadd = 16 - bytekey.__len__() % 16
    keypad = bytearray(keyadd)
    bytekey += keypad
    if bytekey.__len__() > 32:
        bytekey = bytekey[:32]

    decryptor = AES.new(bytekey, mode, IV )
    destr = decryptor.decrypt(bytestr)
    return destr[:len(destr) - destr[-1]]


def encode_string(bytestr, bytekey):

    """
    :param bytestr: Passes in a bytearray to encrypt
    :param bytekey: passes in a bytearray used for encryption
    :return: returns an encoded bytearray
    """

    add = 16 - bytestr.__len__() % 16
    pad = bytearray(add)
    pad[-1] = add
    bytestr+= pad
    keyadd = 16 - bytekey.__len__() % 16
    keypad = bytearray(keyadd)
    bytekey += keypad
    mode = AES.MODE_CBC
    IV = 16 * '\x00'
    if bytekey.__len__() > 32:
        bytekey = bytekey[:32]
    encryptor = AES.new(bytekey, mode, IV)
    enstr = encryptor.encrypt(bytestr)
    return enstr




def encrypt_file(file, key):
    """
    :param file: Passes in the filename for encryption
    :param key: Passes in a bytearray used to encrypt the file
    :return: returns true or false depending if the file was successfully encrypted
    This method will create a new file with the suffix .enc which is the encoded version of the original file
    """
    try:
        f = open(file, 'rb')
    except IOError:
        print('There was an error opening the file!')
        return False
    encname = file + ".enc"
    encf = open(encname, 'wb')
    # line = f.readlines()
    # for x in line:
    #     encf.write(str(secret_string(x, key)))
    encf.write(encode_string(f.read(), key))
    return True

def decrypt_file(file, key):
    """
    :param file: Passes in the filename of an encoded file
    :param key: Passes in a bytearray used to decode the file
    :return: returns true or false depending on if the decryption was successful
    This method will create a new file with the prefix DEC_ which is the decoded version of the encrypted file (A.K.A. the original file)
    """
    if(file[-1] == "c" and file[-2] == "n" and file[-3] == "e" and file[-4] == "."):
        f = open(file, "rb")
        decname = "DEC_" + file
        decname = decname[:decname.__len__()-4]
        decf = open(decname, 'wb')
        # line = [eval(tmp) for tmp in f.readlines()]
        # for x in line:
        #     decf.write(decode_string(x, key))
        decf.write(decode_string(f.read(), key))
        return True
    return False

if __name__ == "__main__":
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    secret_string("hello", key)

def set_counter():
    global counter


def index(request):
    if request.method == "POST" and request.POST.get("unencryptedtext") != None:
        passDict = {}
        unencrypted_text = request.POST.get("unencryptedtext")
        function = request.POST.get("Function")
        if function == "Encrypt":
            encode = True
        else:
            encode = False
        random_generator = Random.new().read

        correct = passDict.__contains__(unencrypted_text)
        if correct:
            key = passDict[unencrypted_text]
        else:
            key = RSA.generate(1024, random_generator)
            passDict[unencrypted_text] = key
        temp = counter
        encode = True
        if encode == True:
            encode = False
            data = secret_string(unencrypted_text, RSA.generate(1024, random_generator))
            data = str(data)
            correct = passDict.__contains__(data)
            return render(request, 'encryption.html',{
                          'data':data ,
                            'key':key,
                            'encode':encode
            })

        else:
            data = decode_string(unencrypted_text, passDict[unencrypted_text])
            data = str(data)
            correct = passDict.__contains__(data)
            return render(request, 'encryption.html', {
                'data': data,
                'key': passDict[data],
                'encode': encode,
                'correct': correct
            })
    else:
        return render(request, 'encryption.html')

