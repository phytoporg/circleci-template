import unittest
import subtracter
import random

class SubtracterTests(unittest.TestCase):
    def test_subtracter_first(self):
        s = subtracter.Subtracter(10, 1)
        self.assertEqual(s.difference(), 9)

    def test_subtracter_lots(self):
        for i in range(1000):
            a, b = random.uniform(0, 1000), random.uniform(0, 1000)
            s = subtracter.Subtracter(a, b)
            self.assertEqual(s.difference(), a - b)
