import importlib
main = importlib.import_module('Medium.7_reverse_integer.main')


def test_1():
    x = 123
    assert main.Solution().reverse(x) == 321


def test_2():
    x = -123
    assert main.Solution().reverse(x) == -321


def test_3():
    x = 120
    assert main.Solution().reverse(x) == 21


def test_4():
    x = 1
    assert main.Solution().reverse(x) == 1


def test_5():
    x = 1534236469
    assert main.Solution().reverse(x) == 0

