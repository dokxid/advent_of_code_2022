from unittest import TestCase
from unittest import skip
from icecream import ic

import constants
from day8 import *


class Test(TestCase):
    
    def test_count_true(self):
        temp_bool = [[True, False, False, False, False],
                     [True, True, False, False, False],
                     [True, True, True, False, False],
                     [True, True, False, False, False],
                     [True, False, False, False, False]]
        self.assertEqual(9, count_true(temp_bool))
    
    def test_mark(self):
        temp_bool = [[False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False],
                     [False, False, False, False, False]]
        mark([True, False, False, False, False], temp_bool, 0)
        mark([True, True, False, False, False], temp_bool, 1)
        mark([True, True, True, False, False], temp_bool, 2)
        mark([True, True, False, False, False], temp_bool, 3)
        mark([True, False, False, False, False], temp_bool, 4)
        self.assertTrue(temp_bool == [[True, False, False, False, False],
                                      [True, True, False, False, False],
                                      [True, True, True, False, False],
                                      [True, True, False, False, False],
                                      [True, False, False, False, False]])
    
    def test_reverse(self):
        temp_data = [['3', '0', '4', '7', '3', '2', '1']]
        temp_data_bool = [[False, False, False, False, False, False, False]]
        for i in range(temp_data.__len__()):
            temp = temp_data[i][:]
            temp.reverse()
            mark(visible_trees(temp_data[i]), temp_data_bool, i)
            mark(visible_trees(temp), temp_data_bool, i, rev=True)
        self.assertEqual([[True, False, True, True, True, True, True]], temp_data_bool)
    
    def test_mark_exc(self):
        try:
            temp_bool = [[False, False, False, False]]
            mark([True, False, False, False, False], temp_bool, 0)
            self.fail()
        except AssertionError:
            self.assertEqual(1, 1)
    
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
    
    def test_part2_mock_distance(self):
        a = constants.parse_int("1233121201\n"
                                "2312233142\n"
                                "3231022313\n"
                                "4332111144\n"
                                "5313204125\n"
                                "6101243406\n"
                                "7323120347\n"
                                "8202003448\n"
                                "9213001029\n"
                                "2142214121")
    
    def test_part2_north(self):
        a = constants.parse_int("1233121201\n"
                                "2312233142\n"
                                "3231022313\n"
                                "4332111144\n"
                                "5313204125\n"
                                "6101243406\n"
                                "7323120347\n"
                                "8202003448\n"
                                "9213001029\n"
                                "2142214121")
        ic(part2(a, "N"))
    
    def test_part2_east(self):
        a = constants.parse_int("1233121201\n"
                                "2312233142\n"
                                "3231022313\n"
                                "4332111144\n"
                                "5313204125\n"
                                "6101243406\n"
                                "7323120347\n"
                                "8202003448\n"
                                "9213001029\n"
                                "2142214121")
        ic(part2(a, "E"))
    
    def test_part2_south(self):
        a = constants.parse_int("1233121201\n"
                                "2312233142\n"
                                "3231022313\n"
                                "4332111144\n"
                                "5313204125\n"
                                "6101243406\n"
                                "7323120347\n"
                                "8202003448\n"
                                "9213001029\n"
                                "2142214121")
        ic(part2(a, "S"))
    
    def test_part2_west(self):
        a = constants.parse_int("1233121201\n"
                                "2312233142\n"
                                "3231022313\n"
                                "4332111144\n"
                                "5313204125\n"
                                "6101243406\n"
                                "7323120347\n"
                                "8202003448\n"
                                "9213001029\n"
                                "2142214121")
        ic(part2(a, "W"))
    
    def test_part2_mock_2(self):
        a = constants.parse_int("30373\n"
                                "25512\n"
                                "65332\n"
                                "33549\n"
                                "35390")
        self.assertEqual(8, part2(a)[0])
    
    def test_part2_mock_3(self):
        a = constants.parse_int("30373\n"
                                "25512\n"
                                "65332\n"
                                "33349\n"
                                "35390")


class TestDistance(TestCase):

    def test_distance_trees(self):
        a = [1, 2, 3, 4, 5]
        self.assertEqual(4, distance_trees(a))

    def test_distance_one(self):
        a = [2]
        self.assertEqual(0, distance_trees(a))

    def test_distance_two(self):
        a = [2, 3]
        self.assertEqual(1, distance_trees(a))

    def test_distance_three(self):
        a = [2, 3, 4]
        self.assertEqual(2, distance_trees(a))

    def test_distance_trees_same_lower_height(self):
        a = [1, 2, 2, 2, 2]
        self.assertEqual(1, distance_trees(a))

    def test_distance_trees_same_higher_height(self):
        a = [3, 2, 2, 2, 2]
        self.assertEqual(4, distance_trees(a))
        
    def test_distance_trees_reverse(self):
        a = [5, 4, 3, 2, 1]
        self.assertEqual(1, distance_trees(a))
        