# Mike Verdicchio, mpv3ms
# CS 3240 -- Advanced Software Development
# Lab 2 -- test_lab2_2.py
# February 1, 2016

import unittest
from Lab2.set import OurSet


class TestSet(unittest.TestCase):

    def setUp(self):
        self.set1 = OurSet([1, 2, 3])
        self.set2 = OurSet([3, 4, 5])
        self.union = OurSet([1, 2, 3, 4, 5, 6])
        self.intersection = OurSet([3])

    def test_union(self):
        # U1: Test union() between two OurSet objects that are each of length 3
        union = self.set1.union(self.set2)
        self.assertEquals(union, self.union, "The union was not created correctly.")

    def test_intersection(self):
        # I1: Test intersection() between two OurSet objects that are each of length 3
        intersection = self.set1.intersection(self.set2)
        self.assertEquals(intersection, self.intersection, "The intersection was not created correctly.")


if __name__ == '__main__':
    unittest.main()

