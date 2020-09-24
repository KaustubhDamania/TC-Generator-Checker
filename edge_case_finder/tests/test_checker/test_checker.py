from checker import Checker
from .input_fn import *
import unittest
import os

class SimpleTest(unittest.TestCase):

    def test1(self):
        os.chdir('tests/test_checker')
        checker = Checker('./test1_correct.out', 'python3 test1_soln.py', input_fn1)
        self.assertTrue(checker.check_randomised(100))

    def test2(self):
        checker = Checker('./test2_correct.out', './test2_soln.out', input_fn2)
        self.assertFalse(checker.check_randomised(100))
        

if __name__ == '__main__':
    unittest.main()
