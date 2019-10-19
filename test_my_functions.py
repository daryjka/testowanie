import my_function


def test_add():
    assert my_function.add(2.5, 0.5) == 3
    assert my_function.add(7, 3) == 10
    assert my_function.add(-7, -3) == -10
# zrobiliśmy test jednostkowy= zgrupowanie asercji


def test_multi():
    assert my_function.multi(2.5, 0.5) == 1.25
    assert my_function.multi(7, 3) == 21
    assert my_function.multi(-7, 3) == -21
# drugi test jednostkowy


def test_invert_word():
    assert my_function.invert_word("") == ""
    assert my_function.invert_word("asd") == "dsa"


def test_is_palindrome():
    assert my_function.is_palindrome("ala")
    assert my_function.is_palindrome("kobyłamamałybok")
    assert not my_function.is_palindrome("as")


def test_sq():
    assert my_function.sq(0) == 0
    assert my_function.sq(3) == 9
    assert my_function.sq(-2) == 4
# test_multi()
# test_add()
# test_invert_word()
# test_is_palindrome()
# zakomentowane, bo zaczynamy używać pytest- zainstalowaliśmy biblioteke