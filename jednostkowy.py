def add(x, y):
    return x + y


def test_add():
    assert add(2.5, 0.5) == 3
    assert add(7, 3) == 10
    assert add(-7, -3) == -10
# zrobiliśmy test jednostkowy= zgrupowanie asercji


def multi(x, y):
    return x * y


def test_multi():
    assert multi(2.5, 0.5) == 1.25
    assert multi(7, 3) == 21
    assert multi(-7, 3) == -21
# zrobiliśmy test jednostkowy


test_multi()
test_add()