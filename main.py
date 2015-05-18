from streams.flow import Flow
from streams.sink import Sink
from streams.source import Source

import string
import resource
import time

def done(): print("done")
def log(line): return len(line)

# Create source, flow and stream
log = open('test/fixtures/es.log', encoding='utf-8')

source = Source.from_file(log)

filter = Flow.filter(lambda i: i.startswith("Caused by: org.elasticsearch.indices.IndexMissingException"))

sink = Sink.reduce(0, lambda t, i: t + 1)

flow = source \
    .via(filter) \
    .to(sink)

res = flow.run(done)
print("---")
print("total: " + str(res))

