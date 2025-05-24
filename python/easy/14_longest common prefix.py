from typing import List


class Solution:
    """
    Grade[Easy]
    Topics[String, Trie]

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Time complexity: O(n × m)
        Space complexity: O(m)
        """
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)
