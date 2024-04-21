from Medium.longest_palindromic_substring_5.main import Solution


def test_1():
    s = 'babaddfbfb'
    assert Solution().longestPalindrome(s) == 'bab'


def test_2():
    s = 'cbbd'
    assert Solution().longestPalindrome(s) == 'bb'


def test_3():
    s = 'b'
    assert Solution().longestPalindrome(s) == 'b'


def test_4():
    s = 'ba'
    assert Solution().longestPalindrome(s) == 'b'
