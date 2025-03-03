from collections import Counter, defaultdict
from typing import List


class Solution:
    """BAD SOLUTION"""
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=len)
        current_length = 0
        current_group_index = -1
        groups = [[]]
        for s in strs:
            if current_length < len(s):
                current_length = len(s)
                current_group_index += 1
            for group in groups[current_group_index:]:
                if (group and Counter(group[0]) == Counter(s)) or not group:
                    group.append(s)
                    break
            else:
                groups.append([s])
        return groups


strs = ["abets","bead","remain","betas","abed","baste","airline","leading","beast","dealing","beats","airmen","marine","single","bade","aligned"]
s = Solution()
result = s.groupAnagrams(strs)
print(strs)


class Solution:
    def groupAnagrams(self, strs):
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
        """
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())