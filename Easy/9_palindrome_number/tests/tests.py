import importlib
main = importlib.import_module('Easy.9_palindrome_number.main')


def test_1():
    assert main.Solution().isPalindrome(121)


def test_2():
    assert not main.Solution().isPalindrome(-121)


def test_3():
    assert not main.Solution().isPalindrome(10)

