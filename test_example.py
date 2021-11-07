import example

def test_success():
    assert example.add_one(5) == 6

def test_failure():
    assert example.add_one(6) == 6

def test_exception():
    assert example.add_one(None) == 1
