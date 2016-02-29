# Mike Verdicchio, mpv3ms
# CS 3240 -- Advanced Software Development
# Lab 3 -- lab3_part1.py
# February 8, 2016

from Crypto.Hash import SHA256

if __name__ == "__main__":
    dictionary = {}
    print("Please load the username/password of all users.")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    hashedPass = SHA256.new(str.encode(password)).hexdigest()
    while password != '':
        if username not in dictionary:
            dictionary.update({username:hashedPass})
        print()
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        hashedPass = SHA256.new(str.encode(password)).hexdigest()

    print()
    print("Please log in.")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    hashedPass = SHA256.new(str.encode(password)).hexdigest()

    if username in dictionary:
        if hashedPass == dictionary.get(username):
            print("login succeeds")
        else:
            print("login fails")
    else:
        print("user not found")