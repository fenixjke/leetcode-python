from Medium.longest_substring_without_repeating_characters_3.main import Solution


def test_1():
    s = 'abcabcbb'
    assert Solution().lengthOfLongestSubstring(s) == 3


def test_2():
    s = 'bbbbb'
    assert Solution().lengthOfLongestSubstring(s) == 1


def test_3():
    s = 'pwwkew'
    assert Solution().lengthOfLongestSubstring(s) == 3


def test_4():
    s = ' '
    assert Solution().lengthOfLongestSubstring(s) == 1


def test_5():
    s = 'dvdf'
    assert Solution().lengthOfLongestSubstring(s) == 3


def test_6():
    s = 'anviaj'
    assert Solution().lengthOfLongestSubstring(s) == 5
