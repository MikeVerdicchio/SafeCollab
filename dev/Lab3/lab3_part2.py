# Mike Verdicchio, mpv3ms
# CS 3240 -- Advanced Software Development
# Lab 3 -- lab3_part2.py
# February 8, 2016

import os
import json

if __name__ == "__main__":
    files = os.listdir()
    dictionary = {}
    for file in files:
        if not os.path.isdir(file):
            text = open(file, 'r')
            numLines = len(text.readlines())
            if file not in dictionary:
                dictionary.update({file:numLines})

    writer = open('file_info.txt', 'w')
    writer.write(json.dumps(dictionary))