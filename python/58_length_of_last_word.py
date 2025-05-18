class Solution:
    """
    Grade[Easy]
    Topics[String]

    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.
    """
    def lengthOfLastWord(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        for word in reversed(s.split(' ')):
            if word:
                return len(word)
