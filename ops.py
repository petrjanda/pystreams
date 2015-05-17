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

