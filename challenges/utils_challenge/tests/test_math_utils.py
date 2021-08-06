from utils.math_utils import *

def test_add_positive():
    num_one = 1
    num_two = 1
    assert add(num_one, num_two) == 2

def test_add_negative():
    num_one = 1
    num_two = 2
    assert add(num_one, num_two) != 2

def test_multiply_positive():
    num1 = 2
    num2 = 3
    assert multiply(num1, num2) == 6

def test_multiply_negative():
    num1 = 2
    num2 = 3
    assert multiply(num1, num2) != 4