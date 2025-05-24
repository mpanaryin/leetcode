class Solution:
    """
    Grade[Medium]
    Topics[]
    Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.

    Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the
    sum of all available primes. If no prime numbers can be formed, return 0.

    A prime number is a natural number greater than 1 with only two factors, 1 and itself.

    A substring is a contiguous sequence of characters within a string.

    Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally,
    when converting a substring to an integer, any leading zeros are ignored.

    Constraints:
        1 <= s.length <= 10
        s consists of only digits.
    """

    def sumOfLargestPrimes(self, s: str) -> int:
        prime_numbers = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                num = int(s[i:j])
                if self.is_prime(num):
                    prime_numbers.add(num)

        return sum(sorted(prime_numbers)[-3:])

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
