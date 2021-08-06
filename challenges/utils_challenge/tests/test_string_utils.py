from utils.string_utils import *

def test_string_repeater_positive():
    character = "a"
    cout = 4
    assert string_repeater(character, cout) == "aaaa"

def test_string_repeater_negative():
    character = "a"
    cout = 5
    assert string_repeater(character, cout) != "aaaa"

