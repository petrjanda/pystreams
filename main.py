import time

from flow import Flow
from source import Source

# Create source, flow and stream
source = Source.from_list(["foo","bar","bazra"])

flow = Flow.map(fn = lambda i: len(i)) \
    .filter(lambda i: i != 3) \
    .map(lambda i: "length: " + str(i))

stream = source.via(flow)

# Benchmark
start = time.time()

for i in range(0, 100000):
    next(stream.input)

print(time.time() - start)
