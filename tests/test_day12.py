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
        self.assertEqual({'up': True, 'down': True, 'left': True, 'right': True}, res)
    
    def test_eval_elevation_2(self):
        a = [[2, 5, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual({'up': False, 'down': True, 'left': True, 'right': True}, res)
    
    def test_eval_elevation_3(self):
        a = [[2, 3, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual({'up': True, 'down': True, 'left': True, 'right': True}, res)
    
    def test_eval_elevation_4(self):
        a = [[2, 1, 2],
             [2, 3, 2],
             [2, 2, 2]]
        res = eval_elevation(a)
        self.assertEqual({'up': False, 'down': True, 'left': True, 'right': True}, res)

    def test_dijk_1(self):
        g = {
            (0, 0): [(1, 1), (2, 1)],
            (1, 1): [(2, 2)],
            (1, 2): [(2, 2)],
            (2, 1): [(1, 2)],
            (2, 2): ["END"]
        }
        s = (0, 0)
        e = (2, 2)
        dijk(g, s, e)

    def test_dijk_2(self):
        g = {
            (0, 0): [(1, 1)],
            (1, 1): [(2, 2), (5, 5)],
            (2, 2): [(3, 3)],
            (3, 3): [(4, 4)],
            (4, 4): ["END"],
            (5, 5): [(4, 4)]
        }
        s = (0, 0)
        e = (4, 4)
        dijk(g, s, e)