class Solution:
    """
    Grade[Medium]
    Topics[Hash Table, String, Sliding Window]

    Given a string s, find the length of the longest substring without repeating characters.
    """

    def length_of_longest_substring(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r - l + 1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output
