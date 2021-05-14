#!/usr/bin/env python

import pytest

from sparkbar import sparkbarh_cell

def test_barh_cell_full_cell():
    "Full cell"
    assert sparkbarh_cell(40, 40, 4) == "████"

def test_barh_cell_half_cell():
    "Half cell"
    assert sparkbarh_cell(10, 20, 4) == "██"

def test_barh_cell_zero_cell():
    "Zero cell"
    assert sparkbarh_cell(0, 5, 4) == ""

def test_barh_cell_longer_cell():
    "Longer cell"
    assert sparkbarh_cell(15, 15, 8) == "████████"

def test_barh_cell_partial_cell():
    "Partial cell 10 width"
    assert sparkbarh_cell(55, 100, 10) == "█████▌"

def test_barh_cell_partial_cel2():
    "Partial cell 8 width"
    assert sparkbarh_cell(56, 100, 8) == "████▌"

def test_barh_cell_partial_rounddown():
    "Cells just over a block should round down to nothing"
    assert sparkbarh_cell(1889, 3739, 8) == "████"

def test_barh_cell_less_than_1_block():
    "Partial cell less than 1 block"
    assert sparkbarh_cell(9375, 100000, 4) == "▍"

def test_barh_cell_negativewidth():
    "Raises on negative widths"
    with pytest.raises(Exception) as e_info:
        sparkbarh_cell(5, 5, -1)

def test_barh_cell_large_width():
    "Raises on large widths"
    with pytest.raises(Exception) as e_info:
        sparkbarh_cell(5, 5, 150)

def test_barh_cell_value_exceed_max():
    "Raises on large values"
    with pytest.raises(Exception) as e_info:
        sparkbarh_cell(10, 5, 12)

def test_barh_cell_add_num():
    "Partial cell 10 width"
    assert sparkbarh_cell(55, 100, 10, add_num=True) == "█████▌ 55"

