class Sink:
    @classmethod
    def foreach(self, fn):
        return Sink(fn)

    @classmethod
    def reduce(self, zero, fn):
        def red(item):
            nonlocal zero
            zero = fn(zero, item)

            return zero

        return Sink(red)

    def __init__(self, op):
        self.op = op

    def run(self, source):
        last = None
        while True:
            try:
                last = self.op(next(source))
            except StopIteration:
                return last
