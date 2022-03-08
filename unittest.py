import pytest

def fuc(x):
    return x + 5

def test_answer():
    assert fuc(3)==8
