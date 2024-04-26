class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if Solution.is_out_of_bounds(x):
            return 0

        is_negative = False
        if x < 0:
            x *= -1
            is_negative = True

        result = 0
        while True:
            if x < 10:
                result = result * 10 + x
                break
            x, remainder = divmod(x, 10)
            result = result * 10 + remainder

        if is_negative:
            result = -result

        if Solution.is_out_of_bounds(result):
            return 0
        return result

    @staticmethod
    def is_out_of_bounds(x):
        return not -2 ** 31 <= x < 2 ** 31
