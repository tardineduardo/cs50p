from plates import is_valid


def test_start_with_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("AS32") == True
    assert is_valid("1AB12") == False
    assert is_valid("12CC12") == False
    assert is_valid("CAC12C") == False


def test_max_min():
    assert is_valid("A") == False
    assert is_valid("12") == False
    assert is_valid("AS32") == True
    assert is_valid("") == False


def test_numbers_middle():
    assert is_valid("AB9812") == True
    assert is_valid("AB12D") == False
    assert is_valid("ACB022") == False
    assert is_valid("ACB201") == True



def test_special_chars():
    assert is_valid("AB12!") == False
    assert is_valid("AB@12") == False
    assert is_valid("AB12?") == False
