class Sink:
    def __init__(self, op):
        self.op = op

    def run(self, source):
        co = self.co()
        co.send(None)

        try:
            for i in range(100): 
                co.send(next(source))
        except StopIteration:
            pass

    def co(self):
        while True:
            item = yield
            self.op(item)
