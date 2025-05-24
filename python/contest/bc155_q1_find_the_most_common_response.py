from collections import Counter


class Solution:
    """
    Grade[Medium]

    You are given a 2D string array responses where each responses[i] is an array of strings representing
    survey responses from the ith day.

    Return the most common response across all days after removing duplicate responses within each responses[i].
    If there is a tie, return the lexicographically smallest response.

    A string a is lexicographically smaller than a string b if in the first position where a and b differ,
    string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
    If the first min(a.length, b.length) characters do not differ,
    then the shorter string is the lexicographically smaller one.

    Constraints:
        1 <= responses.length <= 1000
        1 <= responses[i].length <= 1000
        1 <= responses[i][j].length <= 10
        responses[i][j] consists of only lowercase English letters
    """

    def findCommonResponse(self, responses: list[list[str]]) -> str:
        counter = Counter()
        # Убираем все дубли через set
        responses_set = (set(response) for response in responses)

        # Проходимся по сформированному новому списку без дублей и считаем количество определенных слов
        for response in responses_set:
            for word in response:
                counter[word] += 1

        # Сортируем слова в соответствии с условием задачи и отдаём результат
        sorted_counter = sorted(counter.items(), key=self.priority_lex_key)
        return sorted_counter[0][0]

    @staticmethod
    def priority_lex_key(item):
        word, priority = item
        return -priority, word
