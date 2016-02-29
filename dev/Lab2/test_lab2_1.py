# Mike Verdicchio, mpv3ms
# CS 3240 -- Advanced Software Development
# Lab 2 -- test_lab2_1.py
# February 1, 2016

from Lab2.set import OurSet


def test_add_true():
    # A1: Test add() on an OurSet object by adding an element that isn't already in the set.
    set1 = OurSet()
    ret = set1.add(1)
    assert ret == True, "Adding a new element to an OurSet should return True."
    assert len(set1) == 1, "The length of the OurSet should be 1 when the first element is added."


def test_add_false():
    # A2: Test add() on an OurSet object by adding an element that is already in the set.
    set1 = OurSet()
    set1.add(1)
    set1.add(2)
    set1.add(3)
    ret = set1.add(2)
    assert ret == False, "Adding an element that already exists should return False."
    assert len(set1) == 3, "The length after a false add() should not change."


def test_add_list():
    # AL1: Test add_list() by adding a list of elements to an already present OurSet object.
    set1 = OurSet()
    set1.add(1)
    set1.add(2)
    set1.add(3)
    temp_list = [4, 5, 6]
    ret = set1.add_list(temp_list)
    assert ret == True, "Adding a new list should return True if any element was able to be added."
    assert len(set1) == 6, "The length after adding 3 new elements should be 6."

def test_length():
    # L1: Test __len__() to ensure that the correct length of a set is returned
    set1 = OurSet()
    set1.add(1)
    set1.add(2)
    set1.add(3)
    assert len(set1) == 3, "The length after adding 3 new elements should be 3."
