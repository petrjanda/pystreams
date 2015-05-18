from flow import Flow
from sink import Sink
from source import Source

# Create source, flow and stream
source = Source.from_list(["foo", "bar", "bazra", "aha", "fooba"])

first = Flow.filter(lambda i: len(i) != 3) \
    .map(lambda i: i.capitalize())

second = Flow.filter(lambda i: i[0] == "B") \
    .map(lambda i: len(i))

sink = Sink(lambda i: print(i))

stream = source \
        .via(first) \
        .via(second) \
        .to(sink)
