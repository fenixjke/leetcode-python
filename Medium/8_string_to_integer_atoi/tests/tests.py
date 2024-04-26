import importlib
main = importlib.import_module('Medium.8_string_to_integer_atoi.main')


def test_1():
    x = '42'
    assert main.Solution().myAtoi(x) == 42


def test_2():
    x = '   -42'
    assert main.Solution().myAtoi(x) == -42


def test_3():
    x = '4193 with words'
    assert main.Solution().myAtoi(x) == 4193


def test_4():
    x = '9646324351'
    assert main.Solution().myAtoi(x) == 2147483647


def test_5():
    x = 'words and 987'
    assert main.Solution().myAtoi(x) == 0


def test_6():
    x = ''
    assert main.Solution().myAtoi(x) == 0

