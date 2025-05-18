import itertools


class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Sorting, Enumeration]

    You are given an integer array digits, where each element is a digit. The array may contain duplicates.

    You need to find all the unique integers that follow the given requirements:

    The integer consists of the concatenation of three elements from digits in any arbitrary order.
    The integer does not have leading zeros.
    The integer is even.
    For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

    Return a sorted array of the unique integers.

    Constraints:
        3 <= digits.length <= 100
        0 <= digits[i] <= 9
    """

    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        """
        Time Complexity: O(?) - Beats 8.83%
        Space Complexity: O(M) - Beats 5.55%
        """
        permutations = list(
            set(
                [int(f'{num[0]}{num[1]}{num[2]}') for num in itertools.permutations(digits, 3)
                 if num[0] != 0 and num[2] % 2 == 0]
            )
        )
        permutations.sort()
        return permutations

    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        """
        Time complexity: O(n^3+MlogM) - Beats 16.77%
        Space complexity: O(1) - Beats 12.99%
        """
        nums = set()  # Target even set
        n = len(digits)
        # Traverse the indices of three digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Determine whether it meets the condition of the target even number
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        # Converted to an array sorted in ascending order
        res = sorted(list(nums))
        return res

    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        """
        Time complexity: O() - Beats 100%
        Space complexity: O() - Beats 89.91%
        """
        mpp = [0] * 10
        for d in digits:
            mpp[d] += 1
        res = []
        for i in range(1, 10):
            if mpp[i] == 0:
                continue
            mpp[i] -= 1
            for j in range(10):
                if mpp[j] == 0:
                    continue
                mpp[j] -= 1
                for k in range(0, 10, 2):
                    if mpp[k] == 0:
                        continue
                    res.append(i * 100 + j * 10 + k)
                mpp[j] += 1
            mpp[i] += 1
        return res


digits = [2, 1, 3, 0]
s = Solution()
result = s.findEvenNumbers(digits)
print(result)
