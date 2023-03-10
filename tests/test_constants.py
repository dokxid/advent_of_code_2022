from unittest import TestCase
from constants import *
from icecream import ic


class Test(TestCase):
    
    def test_parse_int(self):
        a = """12345\n54321\n12345"""
        self.assertEqual(['12345', '54321', '12345'], parse_int(a))
        
    def test_get_neighbors(self):
        a = [[5, 3, 5, 3, 5],
             [5, 6, 23, 1, 2],
             [5, 'a', 4, "bb", 6],
             [5, 3, True, 3, 5],
             [5, 3, 5, 3, 5]]
        res = get_neighbors(a, 2, 2)
        self.assertEqual([[6, 23, 1], ['a', 4, 'bb'], [3, True, 3]], res)
        
    def test_get_neighbors_out_of_bounds_top_left(self):
        a = [[5, 3, 5, 3, 5],
             [5, 6, 23, 1, 2],
             [5, 'a', 4, "bb", 6],
             [5, 3, True, 3, 5],
             [5, 3, 5, 3, 5]]
        res = get_neighbors(a, 0, 0)
        self.assertEqual([[-1, -1, -1], [-1, 5, 3], [-1, 5, 6]], res)
        
    def test_get_neighbors_out_of_bounds_bottom_right(self):
        a = [[5, 3, 5, 3, 5],
             [5, 6, 23, 1, 2],
             [5, 'a', 4, "bb", 6],
             [5, 3, True, 3, 5],
             [5, 3, 5, 3, 5]]
        res = get_neighbors(a, 4, 4)
        self.assertEqual([[3, 5, -1], [3, 5, -1], [-1, -1, -1]], res)
