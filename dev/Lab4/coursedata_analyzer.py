"""
Mike Verdicchio, mpv3ms
CS 3240 -- Advanced Software Development
Homework 4 -- coursedata_analyzer.py
February 21, 2016
"""
__author__ = "mpv3ms"

import psycopg2


def instructor_numbers(dept_id):
    """ This function returns a dictionary of instructors and how many students they've taught. """
    dictionary = {}
    conn = psycopg2.connect("dbname=course1" + " user=postgres" + " password=uvahoos")
    cur = conn.cursor()
    cur.execute("SELECT instructor, SUM(seatsTaken) from coursedata WHERE deptid='%s' GROUP BY instructor" % dept_id)
    rows = cur.fetchall()

    for row in rows:
        dictionary.update({row[0]: row[1]})

    conn.commit()
    cur.close()
    conn.close()
    return dictionary


if __name__ == '__main__':
    print(instructor_numbers('ECE'))