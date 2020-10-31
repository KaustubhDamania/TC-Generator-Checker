# Soln_test
:tada: This program tests your solution with a given correct / brute force soln to find edge cases where your solution fails.

## Installation
`$ python3 setup.py install`

## Usage


```
$ python -m edge_case_checker.main -h

usage: main.py [-h] [-i INPUT_FN] [--iterations ITERATIONS] [--soln SOLN] [-c CORRECT_SOLN] [-v VERBOSE]

Generate random test cases!

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FN, --input_fn INPUT_FN
                        Input function to generate random test cases.
  --iterations ITERATIONS
                        No. of randomised test cases for which the program will run.
  --soln SOLN           Command to run the soln to be tested.
  -c CORRECT_SOLN, --correct_soln CORRECT_SOLN
                        Command to run the correct soln.
  -v VERBOSE, --verbose VERBOSE
                        Stats for nerds!
```
