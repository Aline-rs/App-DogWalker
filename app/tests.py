from django.test import TestCase
from models import DogWalker
import unittest


# Create your tests here.
class Teste(unittest.TestCase):

    def test_class(self):
        total = DogWalker()
        expected = 16
        given = total.soma(8, 2)
        self.assertEquals(given, expected)


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
