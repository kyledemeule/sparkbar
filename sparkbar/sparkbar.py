#!/usr/bin/env python

import math

def sparkbarh(numbers=[], width=8, max_value=None):
    if len(numbers) == 0:
        return []

    if max_value is None:
        max_value = _find_max_value(numbers)
        if max_value is None:
            return [""] * len(numbers)

    return [_barh_cell(x, max_value, width) for x in iter(numbers)]



def _find_max_value(numbers):
    not_none = [x for x in numbers if x is not None]
    if len(not_none) > 0:
        return max(not_none)
    else:
        return None

def _barh_cell(value, max_value, width):
    BLOCKS = "▏▎▍▌▋▊▉█"
    bar_length = math.floor(width * (value / max_value))
    return BLOCKS[7] * bar_length

