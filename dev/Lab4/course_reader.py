"""
Mike Verdicchio, mpv3ms
CS 3240 -- Advanced Software Development
Homework 4 -- course_reader.py
February 21, 2016
"""
__author__ = "mpv3ms"

import os
import psycopg2
import csv

def load_course_database(db_name, csv_filename):
    """ This function reads data from a csv file and inserts it into the database. """
    if not os.path.exists(csv_filename):
        print("File doesn't exist.")
        return False

    conn = psycopg2.connect("dbname=course1" + " user=postgres" + " password=uvahoos")
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE coursedata")

    with open(csv_filename, 'rU') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute("INSERT INTO coursedata (deptID, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)", tuple(row))

    conn.commit()
    cur.close()
    conn.close()
    return True

if __name__ == '__main__':
    load_course_database('course1', 'seas-courses-5years.csv')