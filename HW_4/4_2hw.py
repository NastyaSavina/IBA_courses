import unittest
import fun2


class MyTestCase(unittest.TestCase):
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

    def test_greaterValue(self):
        """проверка возвращения большего значения"""
        a = fun2.fun(8, 3)
        b = 4
        self.assertGreater(a, b)  # add assertion here



if __name__ == '__main__':
    unittest.main()
