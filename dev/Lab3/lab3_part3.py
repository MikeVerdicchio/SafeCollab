# Mike Verdicchio, mpv3ms
# CS 3240 -- Advanced Software Development
# Lab 3 -- lab3_part3.py
# February 8, 2016

import json

if __name__ == "__main__":
    json_file = open('file_info.txt', 'r')
    data = json.loads(json_file.read())
    for key in data:
        storedLines = data.get(key)
        text = open(key, 'r')
        newLines = len(text.readlines())
        if storedLines != newLines:
            print("The data file stored that %s has %d lines, but it actually has %d lines." % (key, storedLines, newLines))
