class Solution:
    """
    Grade[Medium]
    Topics[String]

    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
    which is then converted into a different digit string.
    To determine how you "say" a digit string, split it into the minimal number of substrings such that each
    substring contains exactly one unique digit. Then for each substring, say the number of digits,
    then say the digit. Finally, concatenate every said digit.

    For example, the saying and conversion for digit string "3322251":
    Given a positive integer n, return the nth term of the count-and-say sequence.
    """

    def countAndSay(self, n: int) -> str:
        """
        Time complexity: O(2ⁿ)
        Space complexity: O(2ⁿ)
        """

        def str_formatter(string):
            counter = 0
            current_char = string[0]
            new_str = ''
            for i, char in enumerate(string):
                if current_char != char and current_char is not None:
                    new_str += f'{counter}{current_char}'
                    current_char = char
                    counter = 1
                else:
                    counter += 1

                if i == len(string) - 1:
                    new_str += f'{counter}{current_char}'
            return new_str

        s = ''
        for i in range(n):
            if not s:
                s = '1'
            else:
                s = str_formatter(s)
        return s


s = Solution()
result = s.countAndSay(4)
