import importlib
main = importlib.import_module('Medium.6_zigzag_conversion.main')


def test_1():
    s = 'PAYPALISHIRING'
    rows = 3
    assert main.Solution().convert(s, rows) == 'PAHNAPLSIIGYIR'


def test_2():
    s = 'PAYPALISHIRING'
    rows = 4
    assert main.Solution().convert(s, rows) == 'PINALSIGYAHRPI'


def test_3():
    s = 'A'
    rows = 1
    assert main.Solution().convert(s, rows) == 'A'


def test_4():
    s = 'AB'
    rows = 1
    assert main.Solution().convert(s, rows) == 'AB'
