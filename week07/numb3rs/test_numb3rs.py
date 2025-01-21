from numb3rs import validate


def test_validate_correct_ips():
    assert validate('12.0.0.0') == True
    assert validate('15.255.255.200') == True
    assert validate('25.255.0.255') == True
    assert validate('199.1.2.3') == True
    assert validate('1.0.111.1') == True
    assert validate('190.255.28.1') == True
    assert validate('811.50.42.723') == False
    assert validate('708.0.255.0') == False


def test_validate_nondigits():
    assert validate('0.1.2.3') == True
    assert validate('cat.0.2.3') == False
    assert validate('0.1.2.dog') == False


def test_validate_too_many_digits():
    assert validate('0.1.2.3') == True
    assert validate('0.1.2222.3') == False
    assert validate('811.50.42.723') == False
    assert validate('0.1111.2.33') == False
    assert validate('0.1.2.3322') == False


def test_validate_not_four_sets():
    assert validate('0.10.200.3') == True
    assert validate('0.10.200.3.4') == False
    assert validate('0.10.200') == False


def test_validate_values_too_high():
    assert validate('0.10.200.3') == True
    assert validate('0.1.2.300') == False
    assert validate('0.1.299.3') == False
    assert validate('299.1.2.3') == False
    assert validate('127.1.2.300') == False


def test_validate_negative():
    assert validate('0.1.2.3') == True
    assert validate('0.-10.2.100') == False
    assert validate('0.100.2.-100') == False

