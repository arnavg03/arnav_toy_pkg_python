"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from arnav_toy_pkg.example import quick_sort

def test_quick_sort_standard():
    """Test standard list sorting."""
    my_list = [34, 7, 23, 32, 5, 62, 32]
    assert quick_sort(my_list) == [5, 7, 23, 32, 32, 34, 62]

def test_quick_sort_empty():
    """Test empty list."""
    assert quick_sort([]) == []

def test_quick_sort_single():
    """Test list with one element."""
    assert quick_sort([1]) == [1]