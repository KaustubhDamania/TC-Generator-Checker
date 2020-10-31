from random import randint, seed
seed(randint(1,100))

def input_fn():
    t = randint(1, 3)
    testcase = str(t) + '\n'
    for i in range(t):
        n = randint(1,15)
        arr = [str(randint(-100,100)) for i in range(n)]
        testcase += '{}\n{}\n'.format(n,' '.join(arr))
    return testcase
