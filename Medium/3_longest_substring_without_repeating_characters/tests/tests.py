import importlib
main = importlib.import_module('Medium.3_longest_substring_without_repeating_characters.main')


def test_1():
    s = 'abcabcbb'
    assert main.Solution().lengthOfLongestSubstring(s) == 3


def test_2():
    s = 'bbbbb'
    assert main.Solution().lengthOfLongestSubstring(s) == 1


def test_3():
    s = 'pwwkew'
    assert main.Solution().lengthOfLongestSubstring(s) == 3


def test_4():
    s = ' '
    assert main.Solution().lengthOfLongestSubstring(s) == 1


def test_5():
    s = 'dvdf'
    assert main.Solution().lengthOfLongestSubstring(s) == 3


def test_6():
    s = 'anviaj'
    assert main.Solution().lengthOfLongestSubstring(s) == 5
