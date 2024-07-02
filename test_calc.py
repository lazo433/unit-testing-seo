import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)

    def test_mul(self):
        self.assertEqual(self.calc.div(2, 3), 0)

    def test_mul(self):
        self.assertEqual(self.calc.pow(2, 3), 8)

    def test_mul(self):
        self.assertEqual(self.calc.sqrt(4), 2)

    
