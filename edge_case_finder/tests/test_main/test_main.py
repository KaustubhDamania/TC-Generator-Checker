import unittest
import os
from subprocess import check_output

class SimpleTest(unittest.TestCase):

    def test(self):
        # os.chdir('tests/test_main')
        command = 'python3 main.py -i tests/test_main/test1_input_fn.py --soln "python3 tests/test_main/test1_soln.py" -c tests/test_main/test1_correct.out'
        print(check_output(command, shell=True).decode())
        self.assertTrue(True)
    def test1(self):
        # os.chdir('tests/test_main')
        command = 'python3 main.py -i tests/test_main/test2_input_fn.py --soln "./tests/test_main/test2_soln.out" -c ./tests/test_main/test2_correct.out'
        print(check_output(command, shell=True).decode())
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
