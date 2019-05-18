import unittest
import adder
import random
from time import sleep

class SubtracterTests(unittest.TestCase):
    def test_adder_first(self):
        s = adder.Adder(10, 1)
        self.assertEqual(s.sum(), 11)

    def test_adder_lots(self):
        for i in range(100):
            a, b = random.uniform(0, 1000), random.uniform(0, 1000)
            s = adder.Adder(a, b)
            self.assertEqual(s.sum(), a + b)
            sleep(0.05)
