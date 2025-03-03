class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
        The returned integer should be non-negative as well.

        You must not use any built-in exponent function or operator.

        For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
        """
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


s = Solution()
print(s.mySqrt(5))
