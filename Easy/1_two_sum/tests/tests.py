import importlib
main = importlib.import_module('Easy.1_two_sum.main')


def test_1():
    assert main.Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_2():
    assert main.Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_3():
    assert main.Solution().twoSum([3, 3], 6) == [0, 1]

