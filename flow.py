from ops import MapOp, FilterOp

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

