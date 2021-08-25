import unittest


class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('bar', 'BAR')

if __name__ == '__main__':
    unittest.main()