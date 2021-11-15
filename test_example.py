import pytest

import example

def test_success():
    assert example.add_one(5) == 6

@pytest.mark.xfail
def test_failure():
    assert example.add_one(6) == 6

@pytest.mark.xfail
def test_exception():
    assert example.add_one(None) == 1
