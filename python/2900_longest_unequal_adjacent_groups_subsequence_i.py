class Solution:
    """
    Grade[Easy]
    Topics[Array, String, Dynamic Programming, Greedy]

    You are given a string array words and a binary array groups both of length n,
    where words[i] is associated with groups[i].

    Your task is to select the longest alternating subsequence from words.
    A subsequence of words is alternating if for any two consecutive strings in the sequence,
    their corresponding elements in the binary array groups differ. Essentially,
    you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

    Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1]
    denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and
    then find the words corresponding to these indices.

    Return the selected subsequence. If there are multiple answers, return any of them.

    Note: The elements in words are distinct.

    Constraints:
        1 <= n == words.length == groups.length <= 100
        1 <= words[i].length <= 10
        groups[i] is either 0 or 1.
        words consists of distinct strings.
        words[i] consists of lowercase English letters.
    """

    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Time Complexity: O(N) - Beats 100%
        Space Complexity: O(M) - Beats 65.57%
        """
        length = len(words)
        i = 1
        current_state = groups[0]
        res = [words[0]]
        while i != length:
            if current_state != groups[i]:
                current_state = groups[i]
                res.append(words[i])
            i += 1
        return res


words = ["apple", "banana", "cherry", "date", "elderberry"]
groups = [0, 1, 1, 0, 1]
s = Solution()
result = s.getLongestSubsequence(words, groups)
print(result)
