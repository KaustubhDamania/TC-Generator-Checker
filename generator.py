class Generator:
    def __init__(self, tests_count, input_fn):
        self.tests_count = tests_count
        self.input_fn = input_fn

    def generate(self, file_path=None):
        testcase = str(self.tests_count) + '\n'
        for t in range(self.tests_count):
            testcase += self.input_fn()
        if file_path:
            with open(file_path, 'w') as f:
                f.write(testcase)
        return testcase
