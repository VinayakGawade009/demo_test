import sys
import os
# Add src to path so we can import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from utils import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2
