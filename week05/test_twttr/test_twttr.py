import pytest

from twttr import shorten

def test_word():
    assert shorten("pneumonoultramicroscopicsilicovolcanoconiosis") == "pnmnltrmcrscpcslcvlcncnss"

def test_sentence():
    assert shorten("The quick brown fOX Jumps Over the lazy dOG") == "Th qck brwn fX Jmps vr th lzy dG"

def test_specialchars():
    assert shorten("!@#a$E%^i&*()-_=i+o\ |[u]/{/a};u:/?.>") == "!@#$%^&*()-_=+\ |[]/{/};:/?.>"

def test_onlyvowels():
    assert shorten("aeiouy") == "y"

def test_ptbrdiacritics():
    assert shorten("aeiou|teste|áéíóúâêôãõ") == "|tst|áéíóúâêôãõ"

def test_numbers():
    assert shorten("123eduardo") == "123drd"
