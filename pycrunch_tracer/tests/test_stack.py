from pycrunch_tracer.events.method_enter import ExecutionCursor
from pycrunch_tracer.tracing.simple_tracer import CallStack


def test_simple():
    sut = CallStack()
    sut.enter_frame(ExecutionCursor('test', 1))
    sut.enter_frame(ExecutionCursor('test', 2))
    print(sut.top_level_frame_as_clone())
    sut.enter_frame(ExecutionCursor('test', 3))
    print(sut.top_level_frame_as_clone())