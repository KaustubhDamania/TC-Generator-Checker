from subprocess import check_output
from time import time


class Runner:
    def __init__(self, command):
        self.command = command
    def run(self, input_file, stats = False):
        start_time = time()
        output = check_output('{} < {}'.format(self.command, input_file), \
            shell = True).decode().strip()
        end_time = time()
        if stats:
            print('Time taken:', end_time - start_time,'seconds')
        return {
            'output': output,
            'time_taken': end_time - start_time
        }
