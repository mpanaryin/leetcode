from collections import defaultdict


class Solution:
    """
    Grade[Medium]
    Topics[]

    You are given a string word.

    Return the maximum number of non-intersecting substrings of word that are at least four characters long and start
    and end with the same letter.

    A substring is a contiguous non-empty sequence of characters within a string.

    Constraints:
        1 <= word.length <= 2 * 105
        word consists only of lowercase English letters.
    """

    def maxSubstrings(self, word: str) -> int:
        positions = defaultdict(list)
        for index, char in enumerate(word):
            positions[char].append(index)

        new_positions = {}
        for char, positions in positions.items():
            if len(positions) >= 2:
                new_positions[char] = positions

        candidates = []

        for indices in new_positions.values():
            i = 0
            j = 0
            while j < len(indices):
                while j < len(indices) and indices[j] - indices[i] + 1 < 4:
                    j += 1
                if j < len(indices):
                    candidates.append((indices[i], indices[j]))
                    i += 1
                    j = i
                else:
                    break

        candidates.sort(key=lambda x: x[1])

        res, last_end = 0, -1
        for start, end in candidates:
            if start > last_end:
                res += 1
                last_end = end

        return res