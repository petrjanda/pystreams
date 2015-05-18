from streams.flow import Flow
from streams.sink import Sink
from streams.source import Source

# Create source, flow and stream
source = Source.from_list(["babrasta", "foo", "bar", "bazra", "aha", "fooba"])

first = Flow.filter(lambda i: len(i) != 3) \
    .map(lambda i: i.capitalize())

second = Flow.filter(lambda i: i[0] == "B") \
    .map(lambda i: len(i))

sink = Sink.reduce(2, lambda c, i: c + i)

def done(): print("done")

res = source \
    .via(first) \
    .via(second) \
    .to(sink) \
    .run(done)

print("---")
print(res)
