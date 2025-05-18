class Solution:
    """
    Grade[Easy]
    Topics[Math]

    Given two non-negative integers low and high. Return the count of odd numbers
    between low and high (inclusive).
    """

    def count_odds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high % 2 or low % 2)
