import unittest

from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEquals(3, Addition.sum (1,2))

    def test_calculator_subtraction(self):
      self.assertEqual(-1, Subtraction.difference(1,2))

    def test_MathOperations_sum_list(self):
        list = [1,2,3]
        self.assertEqual(6, Addition.sum(valueList))

if __name__ == '__main__':
    unittest.main() 