from utils.string_utils import *

def test_string_repeater_positive():
    character = "a"
    count = 4
    assert string_repeater(character, count) == "aaaa"

# Negatvie test for length
def test_string_repeater_negative():
    character = "a"
    count = 5
    assert string_repeater(character, count) != "aaaa"

# Negative negative test for characters
def test_strin_repeater_negative_character():
    character = "b"
    str_length = 5
    assert string_repeater(character, str_length) != "aaaaa"