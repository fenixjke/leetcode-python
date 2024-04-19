class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring_length = []
        substring = ''
        i = 0
        while i < len(s):
            position = substring.find(s[i])
            if position == -1:
                substring += s[i]
                i += 1
            else:
                substring_length.append(len(substring))
                i = i - len(substring) + 1
                substring = ''

        substring_length.append(len(substring))
        return max(substring_length)




