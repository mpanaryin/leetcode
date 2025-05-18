class Solution:
    def fizz_buzz_generator(self, n):
        """
        Вспомогательная функция-генератор для решения
        Time complexity = O(n)
        Space complexity = O(1)
        """

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                yield "FizzBuzz"
            elif i % 3 == 0:
                yield "Fizz"
            elif i % 5 == 0:
                yield "Buzz"
            else:
                yield str(i)

    def fizzBuzz(self, n: int) -> list[str]:
        """
        Grade[Easy]
        Topics[Math, String, Simulation]

        Given an integer n, return a string array answer (1-indexed) where:

        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.

        Constraints:

        1 <= n <= 10^4

        Time complexity = O(n)
        Space complexity = O(n)
        """
        return list(self.fizz_buzz_generator(n))


s = Solution()
result = s.fizzBuzz(15)
print(result)
