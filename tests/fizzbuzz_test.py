import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("Fizz",fizzbuzz(3))