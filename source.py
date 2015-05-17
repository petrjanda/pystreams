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
