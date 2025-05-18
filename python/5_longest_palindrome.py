class Solution:
    """
    Grade[Medium]
    Topics[Two Pointers, String, Dynamic Programming]

    Given a string s, return the longest palindromic substring in s.
    """
    def longest_palindrome(self, s: str) -> str:
        """
        Time complexity: O(n³)
        Space complexity: O(1)
        """
        def is_palindrome(string):
            if string == string[::-1]:
                return True
            return False
        storage = s[0]
        for f_ind, f_let in enumerate(s):
            for s_ind, s_let in enumerate(s[:f_ind+1]):
                if f_let == s_let and is_palindrome(s[:f_ind+1][s_ind:]):
                    if len(s[:f_ind+1][s_ind:]) > len(storage):
                        storage = s[:f_ind+1][s_ind:]
                        break
        return storage

    def longest_palindrome2(self, s: str) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i - dp[i]:i + dp[i] + 1].replace('#', '')
        return Max_Str
