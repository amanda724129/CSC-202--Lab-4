import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

class BSTTests(unittest.TestCase):
    def test_insert_and_lookup_int(self):
       bst = BinarySearchTree(less_than, None)
       bst = insert(bst, 3)
       bst = insert(bst, 0)
       bst = insert(bst, 9)
       bst = insert(bst, 7)
       self.assertTrue(lookup(bst, 9))
       self.assertTrue(lookup(bst, 0))
       self.assertFalse(lookup(bst, 2))

    def test_insert_and_lookup_str(self):
       bst = BinarySearchTree(less_than, None)
       bst = insert(bst, "frog")
       bst = insert(bst, "car")
       bst = insert(bst, "dog")
       bst = insert(bst, "apple")
       self.assertTrue(lookup(bst, "car"))
       self.assertTrue(lookup(bst, "apple"))
       self.assertFalse(lookup(bst, "big"))

    def test_insert_and_lookup_Point2(self):
       bst = BinarySearchTree(point_less_than, None)
       bst = insert(bst, Point2(0, 1))
       bst = insert(bst, Point2(3, 1))
       bst = insert(bst, Point2(2, 7))
       self.assertTrue(lookup(bst, Point2(3, 1)))
       self.assertTrue(lookup(bst, Point2(2, 7)))
       self.assertFalse(lookup(bst, Point2(5, 6)))

if (__name__ == '__main__'):
 unittest.main() 
