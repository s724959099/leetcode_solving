"""
https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))
        for idx1 in range(len(num1)):
            for idx2 in range(len(num2)):
                result[idx1 + idx2] += int(num1[idx1]) * int(num2[idx2])
        for idx in range(len(result)):
            if result[idx] >= 10:
                result[idx + 1] += result[idx] // 10
                result[idx] %= 10
        result = result[::-1]
        return ''.join(map(str, result)).lstrip('0') or '0'


def assert_num1_num2(num1, num2):
    s = Solution()
    assert s.multiply(num1, num2) == str(int(num1) * int(num2))


if __name__ == '__main__':
    assert_num1_num2('0', '0')
    assert_num1_num2('123', '456')
    assert_num1_num2('456', '123')
    assert_num1_num2('12553', '456')
