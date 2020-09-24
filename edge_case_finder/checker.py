from edge_case_finder.runner import Runner
from edge_case_finder.generator import Generator
from os import remove as delete_file

class Checker:
    def __init__(self, command_correct_soln, command_incorrect_soln, input_fn):
        self.command_correct_soln = command_correct_soln
        self.command_incorrect_soln = command_incorrect_soln
        self.input_fn = input_fn

    # just check the expected output vs actual output for given TC
    def check_one(self, input_file, stats=False):
        correct = Runner(self.command_correct_soln)
        incorrect = Runner(self.command_incorrect_soln)
        expected = correct.run(input_file)
        actual = incorrect.run(input_file)
        if stats and expected['output'] != actual['output']:
            # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
            print('\x1b[5;30;41m' + 'Failed!' + '\x1b[0m')
            print('Expected output', expected['output'])
            print('Actual output', actual['output'])
        return expected['output'] == actual['output']
    
    # check for randomised test cases
    def check_randomised(self, iterations, stats=False):
        generator_obj = Generator(self.input_fn)
        failed_count = 0
        # TODO: optimize this routine using multithreading
        for t in range(iterations): 
            file_name = 'tc' + str(t)
            generator_obj.generate(2, file_path=file_name)
            if not self.check_one(file_name, stats):
                failed_count += 1
            delete_file(file_name)
        if failed_count == 0:
            print('\x1b[6;30;42m' + 'Success! All test cases passed!' + '\x1b[0m')
        else:
            print('\x1b[5;30;41m' + 'Failed! One or more test cases failed!' + '\x1b[0m')
        print('✅: {} ❌: {}'.format(iterations-failed_count, failed_count))
        
        return failed_count == 0

