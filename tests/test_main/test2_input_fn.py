from random import randint, seed
seed(randint(1,100))

def input_fn():
    n = randint(1,15)
    arr = [str(randint(-100,100)) for i in range(n)]
    return '{}\n{}\n'.format(n,' '.join(arr))