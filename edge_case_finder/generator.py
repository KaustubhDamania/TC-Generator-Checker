from random import seed, randint
class Generator:
    def __init__(self, input_fn):
        self.input_fn = input_fn

    def generate(self, max_t, file_path=None):
        seed(randint(1,100))
        # t = randint(1, max_t)
        # testcase = str(t) + '\n'
        # for t in range(t):
        testcase = self.input_fn()
        if file_path:
            with open(file_path, 'w') as f:
                f.write(testcase)
        return testcase
