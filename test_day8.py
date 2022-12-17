from unittest import TestCase
from icecream import ic
from day8 import *


class Test(TestCase):
    
    def test_count_true(self):
        temp_bool = [[True, False, False, False, False],
                     [True, True, False, False, False],
                     [True, True, True, False, False],
                     [True, True, False, False, False],
                     [True, False, False, False, False]]
        self.assertEqual(9, count_true(temp_bool))
    
    def test_mark_trees(self):
        temp_bool = [[False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False]]
        mark_trees([True, False, False, False, False], temp_bool[0])
        mark_trees([True, True, False, False, False], temp_bool[1])
        mark_trees([True, True, True, False, False], temp_bool[2])
        mark_trees([True, True, False, False, False], temp_bool[3])
        mark_trees([True, False, False, False, False], temp_bool[4])
        self.assertTrue(temp_bool == [[True, False, False, False, False],
                                      [True, True, False, False, False],
                                      [True, True, True, False, False],
                                      [True, True, False, False, False],
                                      [True, False, False, False, False]])
    
    def test_mark_trees_exc(self):
        try:
            temp_bool = [False, False, False, False]
            mark_trees([True, False, False, False, False], temp_bool)
            self.fail()
        except AssertionError:
            self.assertEqual(1, 1)
        else:
            self.fail()
    
    def test_visible_trees(self):
        temp = [['3', '0', '3', '7', '3'],
                ['2', '5', '5', '1', '2'],
                ['6', '5', '3', '3', '2'],
                ['3', '3', '5', '4', '9'],
                ['3', '5', '3', '9', '0']]
        self.assertEqual([True, False, False, True, False], visible_trees(temp[0]))
        self.assertEqual([True, True, False, False, False], visible_trees(temp[1]))
        self.assertEqual([True, False, False, False, False], visible_trees(temp[2]))
        self.assertEqual([True, False, True, False, True], visible_trees(temp[3]))
        self.assertEqual([True, True, False, True, False], visible_trees(temp[4]))
