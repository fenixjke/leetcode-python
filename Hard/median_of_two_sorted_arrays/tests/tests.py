from Hard.median_of_two_sorted_arrays.main import Solution


def test_1():
    nums1 = [1, 3]
    nums2 = [2]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2


def test_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5
