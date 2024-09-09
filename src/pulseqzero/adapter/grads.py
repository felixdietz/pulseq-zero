from dataclasses import dataclass
from pulseqzero.adapter import Opts


def make_trapezoid(
    channel,
    amplitude=0,
    area=None,
    delay=0,
    duration=0,
    fall_time=0,
    flat_area=None,
    flat_time=-1,
    max_grad=0,
    max_slew=0,
    rise_time=0,
    system=None,
):
    return Grad()


def make_arbitrary_grad(
    channel,
    waveform,
    delay=0,
    max_grad=0,
    max_slew=0,
    system=None,
):
    return Grad()


@dataclass
class Grad:
    # make_trapezoid
    channel: ...
    amplitude: ...
    rise_time: ...
    flat_time: ...
    fall_time: ...
    area: ...
    flat_area: ...
    delay: ...
    first: ...
    last: ...

    # make_arbitrary_grad
    channel: ...
    waveform: ...
    delay: ...
    tt: ...
    shape_dur: ...
    first: ...
    last: ...
