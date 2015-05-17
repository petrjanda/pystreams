from ops import Source, MapOp, Flow

s = Source.from_list([1,2,3])

m = Flow.map(fn = lambda i: i + 1) \
    .map(lambda i: -i)

stream = s.via(m)

print(next(stream.input))
