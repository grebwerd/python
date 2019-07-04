import unittest
import fibonacci
class testFibonacci(unittest.TestCase):

    def testFirstNumberInFibonacci(self):
        self.assertEqual(3,fibonacci.climbStairs(1), "1 does not equal climbStairs(1)")


if __name__ == ' __main__ ':
    unittest.main()


#command to run the unit test is: python -m unittest testFibonacci.py