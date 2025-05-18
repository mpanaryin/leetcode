from typing import List


class Solution:
    """
    Grade[Hard]
    Topics[Array, Hash Table, String, Bit Manipulation, Enumeration]

    You are given an array of strings ideas that represents a list of names to be used in the process of naming a
    company. The process of naming a company is as follows:
    Choose 2 distinct names from ideas, call them ideaA and ideaB.
    Swap the first letters of ideaA and ideaB with each other.
    If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of
    ideaA and ideaB, separated by a space) is a valid company name.
    Otherwise, it is not a valid name.
    Return the number of distinct valid names for the company.
    """

    def distinct_names(self, ideas: List[str]) -> int:
        ideas_set = set(ideas)
        clean_ideas = list(ideas_set)
        key_value_ideas = dict()
        for idea in clean_ideas:
            value = key_value_ideas.pop(idea[0], None)
            if not value:
                key_value_ideas[idea[0]] = {idea[1:]}
            else:
                key_value_ideas[idea[0]] = value.union({idea[1:]})
        values = list(key_value_ideas.values())
        result = 0
        for i, val1 in enumerate(values):
            for val2 in values[i + 1:]:
                intersection_count = len(val1 & val2)
                result += 2 * (len(val1) - intersection_count) * (len(val2) - intersection_count)
        return result
