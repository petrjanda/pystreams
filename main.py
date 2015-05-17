from flow import Flow
from source import Source

s = Source.from_list([1,2,3])

m = Flow.map(fn = lambda i: i + 1) \
    .filter(lambda i: i > 3) \
    .map(lambda i: -i)

stream = s.via(m)

print(next(stream.input))
