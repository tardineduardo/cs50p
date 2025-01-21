from fuel import convert
from fuel import gauge
import pytest

def test_convert_normal():
	assert convert("1/2") == 50
	assert convert("3/4") == 75
	assert convert("5/6") == 83

def test_convert_value():
	with pytest.raises(ValueError):
	 	convert("cat/2")
	with pytest.raises(ValueError):
		convert("cat")
	with pytest.raises(ValueError):
		convert("cat2")

def test_convert_zero():
	with pytest.raises(ZeroDivisionError):
		convert("4/0")

def test_gauge():
	assert gauge(75) == "75%"
	assert gauge(1) == "E"
	assert gauge(99) == "F"

