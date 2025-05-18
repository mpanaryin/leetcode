class Solution:
    """
    Grade[Easy]
    Topics[String]

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
     determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Решение: просто убираем всё время пары.
    Если когда-то мы не смогли убрать, значит False.
    Думаю этот алгоритм можно доработать переделав 3 replace в 1 через regex.
    Также скорее всего можно сделать всё через 1 список символов и не генерировать постоянно новые строки.
    """

    def is_valid(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if (len(s) % 2):
            return False
        while len(s) != 0:
            new_s = s.replace('[]', '').replace('()', '').replace('{}', '')
            if new_s == s:
                return False
            s = new_s
        return True


class Solution2:
    def is_valid(self, s):
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:  # Если скобка открывающаяся
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # Если скобка закрывающаяся или нет ей пары
                return False
        return len(stack) == 0
