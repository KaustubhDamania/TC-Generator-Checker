from runner import Runner

class Checker:
    def __init__(self, command_correct_soln, command_incorrect_soln):
        this.command_correct_soln = command_correct_soln
        this.command_incorrect_soln = command_incorrect_soln
    def check(self, input_file):
        correct = Runner(command_correct_soln)
        incorrect = Runner(command_incorrect_soln)
        expected = correct.run()
        actual = incorrect.run()
        if expected['output'] == actual['output']:
            print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        else:
            print('\x1b[5;30;41m' + 'Failed!' + '\x1b[0m')
            print('Expected output', expected['output'])
            print('Actual output', actual['output'])
        return expected['output'] == actual['output']
