from unittest import TestCase
from icecream import ic
from day8 import *


class Test(TestCase):
    
    def test_mark_trees(self):
        temp_bool = [[False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False]]
        mark_trees(1, temp_bool[0])
        mark_trees(2, temp_bool[1])
        mark_trees(3, temp_bool[2])
        mark_trees(2, temp_bool[3])
        mark_trees(1, temp_bool[4])
        self.assertTrue(temp_bool == [[True, False, False, False, False],
                                      [True, True, False, False, False],
                                      [True, True, True, False, False],
                                      [True, True, False, False, False],
                                      [True, False, False, False, False]])
    
    def test_visible_trees(self):
        temp = [['3', '0', '3', '7', '3'],
                ['2', '5', '5', '1', '2'],
                ['6', '5', '3', '3', '2'],
                ['3', '3', '5', '4', '9'],
                ['3', '5', '3', '9', '0']]
        self.assertEqual(2, visible_trees(temp[0]))
        self.assertEqual(2, visible_trees(temp[1]))
        self.assertEqual(1, visible_trees(temp[2]))
        self.assertEqual(3, visible_trees(temp[3]))
        self.assertEqual(3, visible_trees(temp[4]))
