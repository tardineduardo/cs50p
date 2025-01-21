from um import count

def test_capitalize():
    assert count("um, um! um...") == 3
    assert count("Um, Um! Um...") == 3

def test_start():
    assert count("um, um no...") == 2

def test_end():
    assert count("hey, um") == 1

def test_words():
    assert count("um, come to the summit") == 1
    assert count("come to the summit") == 0
