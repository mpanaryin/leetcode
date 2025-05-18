from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[String, Backtracking]

    A valid IP address consists of exactly four integers separated by single dots.
    Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245",
    "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
    Given a string s containing only digits, return all possible valid IP addresses that can be
    formed by inserting dots into s. You are not allowed to reorder or remove any digits in s.
    You may return the valid IP addresses in any order.
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, idx, path, res):
        # idx: текущий номер секции
        # path: текущий IP-адрес, который формируется на данном этапе.
        if idx > 4:
            return
        if idx == 4 and not s:
            #  Проверка, если текущий номер секции равен 4 и строка s пуста, то это валидный IP-адрес.
            #  В этом случае добавляем сформированный IP-адрес в список res и завершаем рекурсию.
            res.append(path[:-1])
            return
        for i in range(1, len(s) + 1):
            # Цикл, который перебирает возможные длины секций IP-адреса, начиная с 1 и до конца строки s.
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                #  Проверка, если текущая секция начинается с '0', то это валидная только в том случае,
                #  если она состоит только из '0'. В противном случае, проверяется, что секция не начинается с '0'
                #  и она является целым числом в диапазоне [0, 255].
                self.dfs(s[i:], idx + 1, path + s[:i] + ".", res)
                #  Рекурсивный вызов метода dfs для следующей секции IP-адреса, где s[i:] - оставшаяся часть строки,
                #  idx + 1 - увеличение номера секции, path + s[:i] + "." - обновление текущего IP-адреса,
                #  добавляя текущую секцию, и res передается для сохранения валидных IP-адресов.


s = Solution()
s.restoreIpAddresses("25525511135")