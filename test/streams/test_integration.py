import unittest 

from streams.sink import Sink
from streams.source import Source
from streams.flow import Flow

class PyStreamIntegrationTest(unittest.TestCase):
    def test_reduce(self):
        res = Source.from_list([1,2]).to(Sink.reduce(0, lambda t, i: t + i)).run()
        self.assertEqual(res, 3)

    def test_map(self):
        res = Source.from_list([1]) \
            .via(Flow.map(lambda i: 2*i)) \
            .to(Sink.reduce(0, lambda t, i: t + i)).run()
        self.assertEqual(res, 2)

    def test_on_complete(self):
        done = False

        def is_done():
            nonlocal done
            done = True

        res = Source.from_list([1]) \
            .to(Sink.reduce(0, lambda t, i: t + i)) \
            .run(is_done)

        self.assertTrue(done)
