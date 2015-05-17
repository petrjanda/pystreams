import time

from flow import Flow
from source import Source

# Create source, flow and stream
source = Source.from_list(["foo", "bar", "bazra", "aha", "fooba"])

first = Flow.filter(lambda i: len(i) != 3) \
    .map(lambda i: i.capitalize())

second = Flow.filter(lambda i: i[0] == "B")

stream = source \
        .via(first) \
        .via(second)

# Benchmark
start = time.time()

for i in range(0, 100):
    print(next(stream.input))

print(time.time() - start)
