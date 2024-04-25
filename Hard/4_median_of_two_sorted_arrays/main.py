import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = 0
        merged_nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                merged_nums.extend([nums1[i], nums2[j]])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merged_nums.append(nums2[j])
                j += 1

        if i < len(nums1):
            merged_nums.extend(nums1[i:])
        elif j < len(nums2):
            merged_nums.extend(nums2[j:])

        middle = (len(merged_nums) - 1) / 2.0

        return (merged_nums[int(math.floor(middle))] + merged_nums[int(math.ceil(middle))]) / 2.0
