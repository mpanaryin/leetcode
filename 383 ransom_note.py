from collections import Counter


class Solution:
    """
    Given two strings ransomNote and magazine,
    return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Constraints:

    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of lowercase English letters.
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Time Complexity: O(n+m)
        Space Complexity: O(n+m), O(1) if alphabet is fixed
        """
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        for letter, count in counter1.items():
            if counter2.get(letter, 0) < count:
                return False
        return True
    