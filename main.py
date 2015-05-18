from streams.flow import Flow
from streams.sink import Sink
from streams.source import Source

import string
import resource
import time


# Open log file
log = open('test/fixtures/es.log', encoding='utf-8')

# Helper function ran when stream is done
def on_complete(): 
    log.close()
    print("done")

# Create source, flow and stream
source = Source.from_file(log)
filter = Flow.filter(lambda i: i.startswith("Caused by: org.elasticsearch.indices.IndexMissingException"))
sink = Sink.reduce(0, lambda t, i: t + 1)

result = source.via(filter).to(sink).run(on_complete)

print("---")
print("total: " + str(result))

