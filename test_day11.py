import unittest
from unittest import TestCase
from day11 import *


class TestMonkey(TestCase):
    
    monkeys = []
    
    def setUp(self) -> None:
        monkeys.clear()
    
    def tearDown(self) -> None:
        monkeys.clear()
    
    def test_throw(self):
        
        m0 = Monkey([1, 2])
        m1 = Monkey([3, 4])
        
        monkeys.append(m0)
        monkeys.append(m1)
        ic(monkeys)

        monkeys[0].throw(monkeys[1])
        ic(monkeys)
        
    def test_evaluate_times(self):
        
        m0 = Monkey([2, 3], operation=Operation(operand=4, op="*"))
        m1 = Monkey([3, 4])
        
        monkeys.append(m0)
        monkeys.append(m1)
        
        monkeys[0].evaluate()
        self.assertEqual(8, monkeys[0].items[0])
        
    def test_evaluate_plus(self):
        
        m0 = Monkey([2, 3], operation=Operation(operand=4, op="+"))
        m1 = Monkey([3, 4])
        
        monkeys.append(m0)
        monkeys.append(m1)
        
        monkeys[0].evaluate()
        self.assertEqual(6, monkeys[0].items[0])
        
    def test_evaluate_plus_old(self):
        
        m0 = Monkey([5, 3], operation=Operation(operand="old", op="+"))
        m1 = Monkey([3, 4])
        
        monkeys.append(m0)
        monkeys.append(m1)
        
        monkeys[0].evaluate()
        self.assertEqual(10, monkeys[0].items[0])

    def test_evaluate_times_old(self):
        m0 = Monkey([5, 3], operation=Operation(operand="old", op="*"))
        m1 = Monkey([3, 4])

        monkeys.append(m0)
        monkeys.append(m1)

        monkeys[0].evaluate()
        self.assertEqual(25, monkeys[0].items[0])

    def test_relieve(self):
        m0 = Monkey([9])
        m0.relief()
        self.assertEqual(3, m0.items[0])

    def test_div_test(self):
        
        m0 = Monkey([9, 30], test=3, monkey_true=1, monkey_false=2)
        m1 = Monkey()
        m2 = Monkey()
        
        monkeys.append(m0)
        monkeys.append(m1)
        monkeys.append(m2)
        
        # test false
        ic('false')
        m0.action()
        self.assertEqual(3, m1.items[0])
        self.assertEqual(30, m0.items[0])

        # test true
        ic('true')
        m0.action()
        self.assertEqual(10, m2.items[0])
        self.assertEqual([], m0.items)
        
        