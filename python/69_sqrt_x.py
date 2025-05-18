class Solution:
    """
    Grade[Easy]
    Topics[Math, Binary Search]

    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.

    You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    """

    def mySqrt(self, x: int) -> int:
        if x == 1: return x
        counter = x / 2
        min_to_max = False
        while True:
            current_result = counter * counter
            if current_result == x:
                return int(counter)
            elif current_result > x:
                if min_to_max:
                    return int(counter - 1)
                counter = int(counter / 2)
            elif current_result < x:
                counter += 1
                min_to_max = True

    def mySqrt(self, x):
        """
        Time complexity: O(log x)
        Space complexity: O(1)
        """
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # На выходе right — целая часть sqrt(x)


s = Solution()
print(s.mySqrt(5))
