class Solution:
    """
    Grade[Medium]
    Topics[String, Dynamic Programming]

    A message containing letters from A-Z can be encoded into numbers using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the
    reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
    'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.

    The test cases are generated so that the answer fits in a 32-bit integer.
    """

    def numDecodings(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1  # (1)

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]) <= 9:  # (2)
                dp[i] += dp[i - 1]

            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]
        return dp[len(s)]


s = Solution()
# print(s.numDecodings('10'))
# print(s.numDecodings('12'))
# print(s.numDecodings('226'))
# print(s.numDecodings('06'))
# print(s.numDecodings('2101'))
print(s.numDecodings('1123'))
