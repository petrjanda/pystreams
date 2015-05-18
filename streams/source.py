class SinkAbsent(Exception):
    pass

class Source:
    @classmethod
    def from_list(self, list):
        def gen(list):
            i = 0
            l = len(list)
            while True:
                if i >= l:
                    return

                yield list[i]
                i += 1

        return Source(gen(list))

    def __init__(self, input):
        self.input = input

    def via(self, flow):
        return Source(flow.mat(self.input))

    def to(self, sink):
        self.sink = sink

        return self

    def run(self, on_complete = None):
        if not self.sink:
            raise SinkAbsent("You're trying to run stream without a sink!")

        return self.sink.run(self.input, on_complete)
