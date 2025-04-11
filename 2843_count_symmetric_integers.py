class Solution:
    """
    Grade[Easy]

    You are given two positive integers low and high.

    An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is
    equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

    Return the number of symmetric integers in the range [low, high].

    Constraints:
        1 <= low <= high <= 10^4
    """

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        counter = 0
        for num in range(low, high + 1):
            s_num = str(num)
            len_s_num = len(s_num)
            if len_s_num % 2 == 0:
                if sum(int(i) for i in s_num[len_s_num // 2:]) == sum(int(i) for i in s_num[:len_s_num // 2]):
                    counter += 1
        return counter

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        Time Complexity: O(high-low)
        Space Complexity: O(1)
        """
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res += 1
        return res


low = 1200
high = 1230
s = Solution()
result = s.countSymmetricIntegers(low, high)
print(result)
