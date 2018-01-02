import unittest


class StringMethodsTest(unittest.TestCase):

    def test_uppercase(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        string = 'hello world'
        self.assertEqual(string.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            string.split(2)


if __name__ == '__main__':

    unittest.main()
