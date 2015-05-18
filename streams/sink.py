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

    def run(self, source, on_complete):
        last = None
        while True:
            try:
                last = self.op(next(source))
            except StopIteration:
                if on_complete:
                    on_complete()

                return last
