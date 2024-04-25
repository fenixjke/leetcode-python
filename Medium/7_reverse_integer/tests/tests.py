import importlib
main = importlib.import_module('Medium.7_reverse_integer.main')


def test_1():
    x = 123
    assert main.Solution().convert(x) == 321


def test_2():
    x = -123
    assert main.Solution().convert(x) == -321


def test_3():
    x = 120
    assert main.Solution().convert(x) == 21

