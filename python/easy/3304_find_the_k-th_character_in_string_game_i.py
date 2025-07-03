class Solution:
    """
    Grade[Easy]
    Topics[Math, Bit Manipulation, Recursion, Simulation]

    Alice and Bob are playing a game. Initially, Alice has a string word = "a".

    You are given a positive integer k.

    Now Bob will ask Alice to perform the following operation forever:

    Generate a new string by changing each character in word to its next character in the English alphabet,
    and append it to the original word.
    For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

    Return the value of the kth character in word, after enough operations have been done for word to have at least k
    characters.

    Note that the character 'z' can be changed to 'a' in the operation.

    Constraints:
        1 <= k <= 500
    """

    def kthCharacter(self, k: int) -> str:
        """
        Time Complexity: O() - Beats 58.39%
        Space Complexity: O(<k) - Beats 85.53%
        """
        word = "a"
        while len(word) < k:
            word += ''.join([chr(ord(char) + 1) if char != 'z' else 'a' for char in word])
        return word[k - 1]

    def kthCharacter(self, k: int) -> str:
        """
        Time Complexity: O(log k) - Beats 100%
        Space Complexity: O(1) - Beats 62.61%
        """
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
        return chr(ord("a") + ans)


s = Solution()
result = s.kthCharacter(5)
print(result)
