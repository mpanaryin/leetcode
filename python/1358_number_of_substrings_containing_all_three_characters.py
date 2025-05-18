class Solution:
    """
    Grade[Medium]
    Topics[Hash Table, String, Sliding Window]

    Given a string s consisting only of characters a, b and c.

    Return the number of substrings containing at least one occurrence of all these characters a, b and c.

    Constraints:
    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.
    """

    def numberOfSubstrings(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        # i — индекс начала окна (левая граница)
        res = i = 0
        # count - хранит количество вхождений символов 'a', 'b' и 'c' в текущем окне
        count = {c: 0 for c in 'abc'}
        # j — правая граница окна (индекс конца текущей подстроки)
        for j in range(len(s)):
            # Увеличивается количество текущего символа s[j] в count
            count[s[j]] += 1
            # Проверяется, содержатся ли все три символа ('a', 'b', 'c') в текущем окне
            while all(count.values()):
                # Уменьшается счетчик символа s[i], так как i (левая граница окна) будет сдвигаться вправо
                count[s[i]] -= 1
                # Двигаем левую границу окна вправо, уменьшая его размер, но сохраняя все три символа
                i += 1
            # Добавляем i к res, так как любая подстрока, начинающаяся от 0 до i-1 и заканчивающаяся в j,
            # содержит хотя бы одно вхождение 'a', 'b' и 'c'.
            res += i
        return res


string = "abcabc"
s = Solution()
r = s.numberOfSubstrings(string)
print(r)
