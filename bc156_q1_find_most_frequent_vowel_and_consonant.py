import string
from collections import Counter


class Solution:
    """
    Grade[Easy]

    You are given a string s consisting of lowercase English letters ('a' to 'z').

    Your task is to:

    Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
    Find the consonant (all other letters excluding vowels) with the maximum frequency.
    Return the sum of the two frequencies.

    Note: If multiple vowels or consonants have the same maximum frequency,
    you may choose any one of them. If there are no vowels or no consonants in the string,
    consider their frequency as 0.

    The frequency of a letter x is the number of times it occurs in the string.

    Constraints:
        1 <= s.length <= 100
        s consists of lowercase English letters only.
    """

    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonants = set(string.ascii_lowercase) - vowels
        counter = Counter(s)
        return (max([counter.get(letter, 0) for letter in vowels]) +
                max([counter.get(letter, 0) for letter in consonants]))
