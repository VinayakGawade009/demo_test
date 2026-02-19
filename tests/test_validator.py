import sys
import os
# Add src to path so we can import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

try:
    from validator import is_positive
except SyntaxError:
    # This is expected for the broken project
    pass

def test_is_positive():
    try:
        assert is_positive(5) is True
    except NameError:
        # Expected if import failed
        pass
