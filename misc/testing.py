import pytest

def multi(x):
    return x * 2

def test():
    assert multi(3) == 6
