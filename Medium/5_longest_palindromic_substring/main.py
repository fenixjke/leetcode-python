class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_palindrome_length = len(s)
        while True:
            start = 0
            end = start + max_palindrome_length
            while end <= len(s):
                substring = s[start:end]
                if Solution.is_palindrome(substring):
                    return substring
                start += 1
                end += 1
            max_palindrome_length -= 1

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]




