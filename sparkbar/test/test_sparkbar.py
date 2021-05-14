#!/usr/bin/env python

import pytest

from sparkbar import sparkbarh

def test_empty_list():
	"Test passing in an empty list"
	assert sparkbarh([]) == []
