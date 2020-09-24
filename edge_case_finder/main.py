import argparse
from checker import Checker
from os import remove as delete_file
from os import listdir

def parse_args():
    parser = argparse.ArgumentParser(description='Find edge cases which causes your program to fail by comparing it with a given correct/bruteforce program!')
    parser.add_argument('-i', '--input_fn', help='Input function to generate random test cases.', default='input_fn.py')
    parser.add_argument('--iterations', help='No. of randomised test cases for which the program will run.', type=int, default=100)
    parser.add_argument('--soln', help='Command to run the soln to be tested.')
    parser.add_argument('-c', '--correct_soln', help='Command to run the correct soln.')
    parser.add_argument('-v', '--verbose', help='Stats for nerds!', default=False, type=bool)
    parser.add_argument('-o', '--output-file', help='Edge cases will be stored in this file (default: edge_cases.txt)', default='edge_cases.txt')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    try:
        with open(args.input_fn) as f:
            file_content = f.read()
        with open('temp.py','w') as f:
            f.write(file_content)
        input_fn = __import__('temp').input_fn
    except Exception as e:
        print('Error importing input_fn')
        print(e)
        exit(0)
    finally:
        if 'temp.py' in listdir():
            delete_file('temp.py')
    try:
        checker = Checker(args.correct_soln, args.soln, input_fn)
        checker.check_randomised(args.iterations, stats=args.verbose)
    except Exception as e:
        print('Some error occured with the execution of the files!')
        print(e)
        exit(0)
