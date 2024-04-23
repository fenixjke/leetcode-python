class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        chars_per_row = {}
        addition = 1
        for i in range(numRows):
            chars_per_row[i + 1] = ''
        current_row = 1
        for char in s:
            chars_per_row[current_row] += char
            if 1 <= current_row + addition <= numRows:
                current_row += addition
            if current_row == numRows or current_row == 1:
                addition = -addition

        output = ''
        for i in range(numRows):
            output += chars_per_row[i+1]
        return output

