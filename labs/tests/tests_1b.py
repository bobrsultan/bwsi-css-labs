import pytest
import sys
import os

# Add the lab_1 directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lab_1'))

from lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8
    assert simple_calculator("add", -1, 4) == 3
    assert simple_calculator("add", 0, 9) == 9

def test_subtraction():
    assert simple_calculator("subtract", 10, 3) == 7
    assert simple_calculator("subtract", 17, -3) == 20

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15
    assert simple_calculator("multiply", -1, 1) == -1

def test_division():
    assert simple_calculator("divide", 8, 4) == 2