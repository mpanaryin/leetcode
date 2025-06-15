class Solution:
    """
    Grade[Medium]
    Topics[Math, Greedy]

    You are given an integer num. You will apply the following steps to num two separate times:

    Pick a digit x (0 <= x <= 9).
    Pick another digit y (0 <= y <= 9). Note y can be equal to x.
    Replace all the occurrences of x in the decimal representation of num by y.
    Let a and b be the two results from applying the operation to num independently.

    Return the max difference between a and b.

    Note that neither a nor b may have any leading zeros, and must not be 0.

    Constraints:
        1 <= num <= 10^8
    """
    NUMS = '0123456789'

    def maxDiff(self, num: int) -> int:
        """
        Time complexity: O(1) - Beats 100%
        Space complexity: O(1) - Beats 88.27%
        """
        num = str(num)
        return self.max_value(num) - self.min_value(num)

    def min_value(self, num: str) -> int:
        letters = set(num)
        letters.discard(num[0])
        if num[0] != '1':
            return int(num.replace(num[0], '1'))
        min_val = int(num)
        for let in letters:
            for i in ['0', '1']:
                _num = num.replace(let, i)
                if num[0] == '0' or int(_num) == 0:
                    continue
                min_val = min(min_val, int(_num))
        return min_val

    def max_value(self, num: str) -> int:
        for i, n in enumerate(num):
            if n != '9':
                return int(num.replace(n, '9'))
        return int(num)



nums = 123456
s = Solution()
result = s.maxDiff(nums)
print(result)
