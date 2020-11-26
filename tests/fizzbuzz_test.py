import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz__3_returns_fizz(self):
        self.assertEqual("Fizz",fizzbuzz(3))

    def test_fizzbuzz__5_returns_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))

    def test_fizzbuzz__15_returns_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(15))