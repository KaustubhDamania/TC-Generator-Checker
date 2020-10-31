from random import randint, seed

"""
Generates random test case containing an integer N in 1st line
The second line contains N space seperated integers
"""
def input_fn():
    seed(randint(1,1000))
    t = randint(1, 3)
    testcase = str(t) + '\n'
    for i in range(t):
        n = randint(1,7)
        arr = [randint(1,1000) for i in range(n)]
        testcase += '{}\n{}\n'.format(n, ' '.join(map(str,arr)))
    return testcase
