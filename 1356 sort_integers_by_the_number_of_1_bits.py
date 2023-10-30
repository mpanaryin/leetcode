class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        You are given an integer array arr.
        Sort the integers in the array in ascending order by the number of 1's in their binary
        representation and in case of two or more integers have the same number of 1's
        you have to sort them in ascending order.

        Return the array after sorting it.
        """
        arr.sort()
        arr.sort(key=lambda x: bin(x).count('1'))
        return arr
    