class Solution:
    """
    Grade[Easy]
    Topics[String, Simulation]

    A string s can be partitioned into groups of size k using the following procedure:

    The first group consists of the first k characters of the string, the second group consists of the next k
    characters of the string, and so on. Each element can be a part of exactly one group.
    For the last group, if the string does not have k characters remaining, a character fill is used to complete the
    group.
    Note that the partition is done so that after removing the fill character from the last group (if it exists) and
    concatenating all the groups in order, the resultant string should be s.

    Given the string s, the size of each group k and the character fill, return a string array denoting the
    composition of every group s has been divided into, using the above procedure.

    Constraints:
        1 <= s.length <= 100
        s consists of lowercase English letters only.
        1 <= k <= 100
        fill is a lowercase English letter.
    """

    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        """
        Time Complexity: O(n) - Beats 100%
        Space Complexity: O(n) - Beats 36.31%
        """
        result = []
        start = 0
        str_length = len(s)
        while start < str_length:
            result.append(s[start:start+k])
            start += k

        if str_length % 3 != 0:
            result[-1] += fill * (k - (str_length % k))

        return result



s = Solution()
ss = "abcdefghij"
k = 3
fill = "x"

ss = "umrcmcqqkchpwnudzdoqz"
k = 74
fill = "b"

result = s.divideString(ss, k, fill)
print(result)