from edge_case_finder.runner import Runner
from edge_case_finder.generator import Generator
from os import remove as delete_file
import os

class Checker:
    def __init__(self, command_correct_soln, command_incorrect_soln, input_fn):
        self.command_correct_soln = command_correct_soln
        self.command_incorrect_soln = command_incorrect_soln
        self.input_fn = input_fn

    # just check the expected output vs actual output for given TC
    def check_one(self, input_file, stats=False, out_file=None):
        correct = Runner(self.command_correct_soln)
        incorrect = Runner(self.command_incorrect_soln)
        expected = correct.run(input_file)
        actual = incorrect.run(input_file)
        if expected['output'] != actual['output']:
            # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
            content = '\x1b[5;30;41mFailed!\x1b[0m\n'
            content += 'Test case:\n{}\n'
            content += 'Expected output:\n{}\n'
            content += 'Actual output:\n{}\n\n'
            content = content.format(input_file, expected['output'], actual['output'])
            if stats:
                print(content)
            if out_file:
                with open(out_file, 'a') as f:
                    f.write(content)
            # print('\x1b[5;30;41m' + 'Failed!' + '\x1b[0m')
            # print('Expected output', expected['output'])
            # print('Actual output', actual['output'])
        return expected['output'] == actual['output']
    
    # check for randomised test cases
    def check_randomised(self, iterations, stats=False, out_file=None):
        generator_obj = Generator(self.input_fn)
        failed_count = 0
        folder_name = 'failed_testcases'
        os.makedirs(folder_name, exist_ok=True)
        if out_file:
            with open(out_file,'w') as f:
                pass
        
        # TODO: optimize this routine using multithreading
        for t in range(iterations): 
            file_name = os.path.join(folder_name, 'tc' + str(t))
            generator_obj.generate(2, file_path=file_name)
            if not self.check_one(file_name, stats, out_file):
                failed_count += 1
            else:
                delete_file(file_name)
        if failed_count == 0:
            print('\x1b[6;30;42m' + 'Success! All test cases passed!' + '\x1b[0m')
        else:
            print('\x1b[5;30;41m' + 'Failed! One or more test cases failed!' + '\x1b[0m')
        print('✅: {} ❌: {}'.format(iterations-failed_count, failed_count))
        if failed_count and out_file:
            print('The complete summary can be found in', out_file)
            print('The failed test cases can be found in', folder_name, 'folder')
        return failed_count == 0