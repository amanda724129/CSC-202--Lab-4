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
       
   def test_delete_int(self):
      bst = BinarySearchTree(less_than, None)
      for val in [5, 3, 7, 2, 4, 6, 8]:
         bst = insert(bst, val)
      bst = delete(bst, 2)
      self.assertFalse(lookup(bst, 2))
      self.assertTrue(lookup(bst, 3))

      bst = delete(bst, 4)
      self.assertFalse(lookup(bst, 4))

      bst = delete(bst, 5)
      self.assertFalse(lookup(bst, 5))
      self.assertTrue(lookup(bst, 6)) 

   def test_delete_str(self):
      bst = BinarySearchTree(less_than, None)
      for word in ["frog", "car", "dog", "apple", "zebra"]:
         bst = insert(bst, word)

      bst = delete(bst, "dog") 
      self.assertFalse(lookup(bst, "dog"))
      self.assertTrue(lookup(bst, "car"))
      self.assertTrue(lookup(bst, "frog"))

      bst = delete(bst, "apple")  
      self.assertFalse(lookup(bst, "apple"))

   def test_delete_Point2(self):
      bst = BinarySearchTree(point_less_than, None)
      pts = [Point2(0, 1), Point2(3, 1), Point2(2, 7), Point2(1, 1)]
      for p in pts:
         bst = insert(bst, p)

      bst = delete(bst, Point2(3, 1))
      self.assertFalse(lookup(bst, Point2(3, 1)))
      self.assertTrue(lookup(bst, Point2(2, 7)))

      bst = delete(bst, Point2(0, 1))
      self.assertFalse(lookup(bst, Point2(0, 1)))



if (__name__ == '__main__'):
 unittest.main() 
