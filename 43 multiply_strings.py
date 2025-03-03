class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Given two non-negative integers num1 and num2 represented as strings,
        return the product of num1 and num2, also represented as a string.

        Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
        Без конвертации можно сделать словарь, в котором будет str: int. По типу {'1': 1, '2': 2}.
        Так составить число через + с десятками, сотнями, единицами...
        """
        return str(int(num1) * int(num2))
