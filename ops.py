class Op:
    def mat(self, input):
        return self.gen(input)

class MapOp(Op):
    def __init__(self, fn):
        self.fn = fn

    def gen(self, input):
        while True:
            yield self.fn(next(input))

class FilterOp(Op):
    def __init__(self, pred):
        self.pred = pred

    def gen(self, input):
        while True:
            item = next(input)
            
            if(self.pred(item)):
                yield item

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

    def filter(self, pred):
        return FlowImp(FilterOp(pred), self)

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
