import pytest

@pytest.mark.yuk
def test_pass():
    assert 1 == 1

@pytest.mark.yuk
def test_fail():
    assert 1 == 2

def test_pass_unmarked():
    assert 1 == 1

def test_fail_unmarked():
    assert 1 == 2
