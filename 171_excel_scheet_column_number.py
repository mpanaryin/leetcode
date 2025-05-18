import string


class Solution:
    """
    Grade[Easy]
    Topics[Math, String]

    Given a string columnTitle that represents the column title as appears in an Excel sheet,
    return its corresponding column number.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
    """
    def titleToNumber(self, columnTitle: str) -> int:
        letters_and_values = dict(zip(string.ascii_uppercase, range(1, 27)))
        return sum([26**i * letters_and_values[let] for i, let in enumerate(reversed(columnTitle))])


columnTitle1 = 'B'
columnTitle2 = 'Z'
columnTitle3 = 'ZY'
columnTitle4 = 'FXSHRXW'
s = Solution()
result = s.titleToNumber(columnTitle1)
print(result)
