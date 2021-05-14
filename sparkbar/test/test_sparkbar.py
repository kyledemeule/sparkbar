#!/usr/bin/env python

import pytest

from sparkbar import sparkbarh

def test_empty_list():
    "Test passing in an empty list"
    assert sparkbarh([]) == []

def test_list_with_negative_numbers():
    "Raises on negative numbers"
    with pytest.raises(Exception) as e_info:
        sparkbarh([1, -1, 1])

def test_list_of_none():
    "List full of nones returns blank strings"
    assert sparkbarh([None, None, None]) == ["", "", ""]
