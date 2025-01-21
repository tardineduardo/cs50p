from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value(" Hello") == 0
    assert value("Hello!") == 0
    assert value("hello!!!") == 0


def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value(" Hiii") == 20
    assert value(" hallo!!!") == 20


def test_other():
    assert value("0") == 100
    assert value("!!!") == 100
    assert value("-3") == 100
