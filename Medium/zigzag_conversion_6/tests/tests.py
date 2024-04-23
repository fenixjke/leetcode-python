from Medium.zigzag_conversion_6.main import Solution


def test_1():
    s = 'PAYPALISHIRING'
    rows = 3
    assert Solution().convert(s, rows) == 'PAHNAPLSIIGYIR'


def test_2():
    s = 'PAYPALISHIRING'
    rows = 4
    assert Solution().convert(s, rows) == 'PINALSIGYAHRPI'


def test_3():
    s = 'A'
    rows = 1
    assert Solution().convert(s, rows) == 'A'


def test_4():
    s = 'AB'
    rows = 1
    assert Solution().convert(s, rows) == 'AB'
