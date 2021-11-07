import unittest
import calc


class MyTestCase(unittest.TestCase):
    """Calc test: """

    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after [" + self.shortDescription() + "]")

    def test_divmod(self):
        """ modulo division check """
        self.assertNotEqual(calc.divmod(6, 3), 1)


if __name__ == '__main__':
    unittest.main()
