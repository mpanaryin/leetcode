from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

        Return any possible rearrangement of s or return "" if not possible.
        """
        count_s = Counter(s)
        final_string = ''
        last_added = None
        while count_s:
            max_char = None
            for char in count_s:
                if char != last_added and (max_char is None or count_s[char] > count_s[max_char]):
                    max_char = char
            if not max_char:
                return ''

            if max_char != last_added:
                last_added = max_char
                final_string += max_char
                count_s[max_char] -= 1
                if count_s[max_char] == 0:
                    del count_s[max_char]

        return final_string


s = Solution()
result = s.reorganizeString('aabbcc')
print(result)