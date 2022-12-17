from unittest import TestCase
from constants import *
from icecream import ic


class Test(TestCase):
    def test_parse_int(self):
        a = """12345\n54321\n12345"""
        self.assertEqual(['12345', '54321', '12345'], parse_int(a))
