class Solution:
    """
    Grade[Easy]
    Topics[Array, Bit Manipulation, Sorting, Counting]

    You are given an integer array arr.
    Sort the integers in the array in ascending order by the number of 1's in their binary
    representation and in case of two or more integers have the same number of 1's
    you have to sort them in ascending order.

    Return the array after sorting it.
    """

    def sortByBits(self, arr: list[int]) -> list[int]:
        """
        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        arr.sort()
        arr.sort(key=lambda x: bin(x).count('1'))
        return arr
