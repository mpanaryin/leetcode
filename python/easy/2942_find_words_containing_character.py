class Solution:
    """
    Grade[Easy]
    Topics[Array, String]

    You are given a 0-indexed array of strings words and a character x.

    Return an array of indices representing the words that contain the character x.

    Note that the returned array may be in any order.

    Constraints:
        1 <= words.length <= 50
        1 <= words[i].length <= 50
        x is a lowercase English letter.
        words[i] consists only of lowercase English letters.
    """

    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        """
        Time Complexity: O(N*M) - Beats 100%
        Space Complexity: O(N) - Beats 68.13%
        """
        return [i for i, word in enumerate(words) if x in word]


words = ["leet", "code"]
x = "e"
s = Solution()
result = s.findWordsContaining(words, x)
print(result)
