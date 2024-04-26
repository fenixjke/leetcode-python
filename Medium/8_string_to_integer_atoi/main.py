class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = Solution.step_1_remove_whitespaces(s)
        sign, s = Solution.step_2_read_sign(s)
        number_str = Solution.step_3_read_number(s)
        number = Solution.step_4_convert_to_int(number_str, sign)
        return Solution.step_5_clamp_into_range(number)

    @staticmethod
    def step_1_remove_whitespaces(s):
        while s and s[0] == ' ':
            s = s[1:]
        return s

    @staticmethod
    def step_2_read_sign(s):
        sign = 1
        if s and (s[0] == '+' or s[0] == '-'):
            sign = int(s[0] + '1')
            s = s[1:]
        return sign, s

    @staticmethod
    def step_3_read_number(s):
        result = ''
        for char in s:
            if char.isdigit():
                result += char
            else:
                return result
        return result

    @staticmethod
    def step_4_convert_to_int(s, sign):
        if s == '':
            s = '0'
        return int(s) * sign

    @staticmethod
    def step_5_clamp_into_range(i):
        if i < -2**31:
            i = -2**31
        elif i > 2**31 - 1:
            i = 2**31 - 1
        return i



