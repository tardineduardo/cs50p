from working import convert
import pytest

def test_no_minutes():
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("1 PM to 12 PM") == "13:00 to 12:00"
    assert convert("10 PM to 1 AM") == "22:00 to 01:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_with_minutes():
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("1:00 PM to 12:31 PM") == "13:00 to 12:31"
    assert convert("10:12 PM to 1:00 PM") == "22:12 to 13:00"
    assert convert("12:59 PM to 12:00 AM") == "12:59 to 00:00"

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("8:80 PM to 8:70 AM")
        convert("8:10 PM to 8:70 AM")
        convert("8:80 PM to 8:10 AM")

def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 PM to 14:00 PM")
        convert("13:80 PM to 10:00 PM")
        convert("7:50 PM to 14:70 AM")

def test_no_to():
    with pytest.raises(ValueError):
        convert("13:00 PM 14:00 PM")
        convert("13:80 PM | 10:00 PM")
        convert("7:50 PM - 14:70 AM")
