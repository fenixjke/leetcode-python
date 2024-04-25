import importlib
main = importlib.import_module('Medium.5_longest_palindromic_substring.main')


def test_1():
    s = 'babaddfbfb'
    assert main.Solution().longestPalindrome(s) == 'bab'


def test_2():
    s = 'cbbd'
    assert main.Solution().longestPalindrome(s) == 'bb'


def test_3():
    s = 'b'
    assert main.Solution().longestPalindrome(s) == 'b'


def test_4():
    s = 'ba'
    assert main.Solution().longestPalindrome(s) == 'b'
