class Solution:
    """
    Grade[Medium]
    Topics[String]

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
    like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:
    """

    def convert(self, s: str, numRows: int) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if numRows == 1:
            return s
        array_2d = [[] for i in range(numRows)]
        first_switcher = 0
        limit = numRows
        second_switcher_start_index = numRows - 2
        second_switcher = second_switcher_start_index
        for let in s:
            if first_switcher == limit and second_switcher > 0:
                array_2d[second_switcher].append(let)
                second_switcher -= 1
                if second_switcher == 0:
                    second_switcher = second_switcher_start_index
                    first_switcher = 0
                continue
            array_2d[first_switcher].append(let)
            first_switcher += 1
            if second_switcher_start_index == 0 and first_switcher == 2:
                first_switcher = 0
        return ''.join(a2 for a1 in array_2d for a2 in a1)
