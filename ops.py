class MapOp:
    def __init__(self, fn):
        self.fn = fn

    def mat(self, input):
        def gen(input):
            while True:
                yield self.fn(next(input))

        return gen(input)

class Flow:
    @classmethod
    def map(self, fn):
        return FlowImp(MapOp(fn))

class FlowImp:
    def __init__(self, op, prev = None):
        self.op = op
        self.prev = prev

    def mat(self, input):
        if self.prev:
            input = self.prev.mat(input)

        return self.op.mat(input)

    def map(self, fn):
        return FlowImp(MapOp(fn), self)

class Source:
    @classmethod
    def from_list(self, list):
        def gen(list):
            i = 0
            while True:
                yield list[i]
                i += 1

        return Source(gen(list))

    def __init__(self, input):
        self.input = input

    def via(self, flow):
        return Source(flow.mat(self.input))
