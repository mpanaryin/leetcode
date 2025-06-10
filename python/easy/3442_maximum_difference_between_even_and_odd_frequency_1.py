from collections import Counter


class Solution:
    """
    Grade[Easy]
    Topics[Hash Table, String, Counting]

    You are given a string s consisting of lowercase English letters.

    Your task is to find the maximum difference diff = freq(a1) - freq(a2)
    between the frequency of characters a1 and a2 in the string such that:

    a1 has an odd frequency in the string.
    a2 has an even frequency in the string.
    Return this maximum difference.
    """

    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        max_odd = max(val for val in counter.values() if val % 2 == 1)
        min_even = min(val for val in counter.values() if val % 2 == 0)
        return max_odd - min_even


s = Solution()
result = s.maxDifference("aaaaabbc")
print(result)
