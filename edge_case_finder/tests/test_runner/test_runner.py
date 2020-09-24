from runner import Runner
import unittest
import os

class SimpleTest(unittest.TestCase):

    def test(self):
        os.chdir('tests/test_runner')
        runner_obj = Runner('./test_runner.out')
        with open('test_runner_output1') as f:
            expected_output = f.read()
        self.assertEqual(runner_obj.run('test_runner_input1')['output'],
        expected_output.strip())

    def test1(self):
        runner_obj = Runner('python3 soln.py')
        with open('test_runner_output2') as f:
            expected_output = f.read()
        self.assertEqual(runner_obj.run('test_runner_input2')['output'],
        expected_output.strip())

if __name__ == '__main__':
    unittest.main()
