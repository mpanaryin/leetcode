class Solution:
    """
    Grade[Medium]
    Topics[Math, Bit Manipulation]
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Given two integers dividend and divisor, divide two integers without using multiplication,
        division, and mod operator.

        The integer division should truncate toward zero, which means losing its fractional part.
        For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

        Return the quotient after dividing dividend by divisor.

        Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed
        integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1,
        then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

        This function uses bitwise left shift for multiplication-like operations and subtraction to perform the division.
        It also handles edge cases like division by zero and overflow.
        Please note that this solution works with 32-bit signed integers as specified.

        1.Создание констант INT_MAX и INT_MIN, представляющих верхнюю и нижнюю границы диапазона 32-битных целых чисел.

        2.Проверка случаев, когда делитель равен нулю (вернуть максимальное значение) и когда делимое равно INT_MIN,
        а делитель равен -1 (вернуть максимальное значение, так как деление приведет к переполнению).

        3.Определение флага negative, который будет True, если результат деления должен быть отрицательным.
        Он вычисляется через операцию XOR на знаки делимого и делителя.

        4.Преобразование делимого и делителя в положительные числа для удобства работы.

        5.Создание переменной quotient, которая будет хранить результат деления.

        6.Основной цикл, в котором мы пытаемся вычислить частное. Мы продолжаем цикл, пока делимое больше или равно делителю.

        7.Вложенный цикл для быстрого нахождения наибольшего temp_divisor, который меньше или равен текущему делимому.
        При этом удваиваем делитель и множитель на каждой итерации цикла.
        Это эффективно симулирует битовый сдвиг влево для выполнения умножения на степень двойки.

        8.Вычитание temp_divisor из делимого и добавление к quotient соответствующего значения multiple.
        Это происходит до тех пор, пока текущее делимое не станет меньше делителя.

        9.Возврат результата с учетом флага negative и проверка на переполнение (ограничение диапазона).

        Побитовый сдвиг влево (<<):
        При сдвиге числа влево, все биты числа сдвигаются на определенное количество позиций влево. Новые (нижние) биты, которые становятся "свободными" справа, заполняются нулями. Каждое смещение на одну позицию влево эквивалентно умножению числа на 2. Например, сдвиг числа 5 на 2 позиции влево даст 20 (00000101 << 2 = 00101000).

        Побитовый сдвиг вправо (>>):
        При сдвиге числа вправо, все биты числа сдвигаются на определенное количество позиций вправо. Новые (старшие) биты, которые становятся "свободными" слева, заполняются либо нулями (для положительных чисел), либо единицами (для отрицательных чисел). Каждое смещение на одну позицию вправо эквивалентно целочисленному делению числа на 2. Например, сдвиг числа -16 на 2 позиции вправо даст -4 (11110000 >> 2 = 11111100).
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if divisor == 0:
            return INT_MAX

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        if negative:
            quotient = -quotient

        return max(min(quotient, INT_MAX), INT_MIN)


s = Solution()
result = s.divide(-2147483648, -1)
print(result)