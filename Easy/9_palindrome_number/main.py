class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        initial_number = x
        reversed_number = 0
        while True:
            x, remainder = divmod(x, 10)
            if x == remainder == 0:
                break
            reversed_number = reversed_number * 10 + remainder
        return reversed_number == initial_number
