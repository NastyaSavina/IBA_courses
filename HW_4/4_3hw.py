import unittest
import conc


class MyTestCase(unittest.TestCase):
    def test_concatenation(self):
        self.assertEqual(conc.concatenation(35, 21), 3521)  # add assertion here


if __name__ == '__main__':
    unittest.main()
