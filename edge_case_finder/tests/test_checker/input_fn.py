from random import randint, seed
seed(randint(1,100))

def input_fn1():
    t = randint(1, 3)
    testcase = str(t) + '\n'
    for i in range(t):
        n = randint(1,15)
        k = randint(0,n)
        s = ''.join([str(randint(0,1)) for i in range(n)])
        testcase += '{} {}\n{}\n'.format(n,k,s)
    return testcase

def input_fn2():
    t = randint(1, 3)
    testcase = str(t) + '\n'
    for i in range(t):
        n = randint(1,15)
        arr = [str(randint(-100,100)) for i in range(n)]
        testcase += '{}\n{}\n'.format(n,' '.join(arr))
    return testcase
