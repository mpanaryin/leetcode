class Solution:
    """
    Grade[Easy]
    Topics[Two Pointers, String]

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
    removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """

    def isPalindrome(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        clean_str = ''.join([letter for letter in s.lower() if letter.isalpha()])
        if clean_str == clean_str[::-1]:
            return True
        return False


s = "A man, a plan, a canal: Panama"
sol = Solution()
sol.isPalindrome(s)
