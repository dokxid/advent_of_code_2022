from unittest import TestCase
from day12 import *


class Test(TestCase):
    
    def test_part_1(self):
        return None
        
    def test_eval_elevation_1(self):
        a = [[2, 2, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual([[False, True, False],
                          [True, False, True],
                          [False, True, False]], res)
        
    def test_eval_elevation_2(self):
        a = [[2, 5, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual([[False, False, False],
                          [True, False, True],
                          [False, True, False]], res)
        
    def test_eval_elevation_3(self):
        a = [[2, 3, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual([[False, True, False],
                          [True, False, True],
                          [False, True, False]], res)
        
    def test_eval_elevation_4(self):
        a = [[2, 1, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual([[False, False, False],
                          [True, False, True],
                          [False, True, False]], res)
        