from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[Array, Math]

    The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
    """

    def add_to_array_form(self, num: List[int], k: int) -> List[int]:
        return list(map(lambda n: int(n), list(str(int(''.join(map(lambda n: str(n), num))) + k))))
