import unittest


class CalculationTest(unittest.TestCase):

    def setUp(self):
        self.a = 5
        self.b = 2

    def test_add_two_numbers(self):
        self.assertEqual(self.a + self.b, 7)
